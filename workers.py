import traceback
import sys
from PyQt5 import QtCore
from quetzal import getProjects


class Worker(QtCore.QRunnable):

    def __init__(self, fn, *args, **kwargs):
        print(fn)
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress

    @QtCore.pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        try:
            result = self.fn(
                *self.args, **self.kwargs
            )
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit('done')


class WorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal(str)
    progress = QtCore.pyqtSignal(int)
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(object)


class Updater(Worker):
    def __init__(self, do_debug=False, override=False):
        self.to_update = getProjects()
        self.debug = do_debug
        self.override = override

        if not isinstance(self.debug, bool) or not isinstance(self.override, bool):
            self.reportUnable()

        if self.debug:
            self.debug_flag = 'corvid-debug'
        else:
            self.debug_flag = 'corvid'

        if self.override:
            self.override_flag = '--override'
        else:
            self.override_flag = '--move'

        self._current = ''
        self.status = 'Pending'

        args = ['npx', self.debug_flag, 'pull', self.override_flag]
        self.updating(args)

    def updating(self, args):
        for _inx_, _iteration_ in enumerate(self.to_update):
            self._current = _iteration_['slug']
            try:
                now_updating = run(args, cwd=_iteration_[
                                   'abs_dir'], capture_output=True)
                now_updating.check_returncode()

                self.status = now_updating.stdout
            except CalledProcessError:
                self.status = f"""Error updating {_iteration_}
{CalledProcessError}"""

            if _inx_ == len(self.to_update) - 1:
                self.status = 'Done'
                return self.status
        else:
            self.status = 'main.py: update all failed'

    def reportUnable(self):
        report = {
            'DEBUG': 'NOT VALID',
            'OVERRIDE':  'NOT VALID'
        }

        if isinstance(self.debug, bool):
            report['DEBUG'] = 'OK'
        if isinstance(self.override, bool):
            report['OVERRIDE'] = 'OK'

        return report