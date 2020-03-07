import sys
from PyQt5 import QtCore
from pathlib import Path
from subprocess import (run, CalledProcessError)
from quetzal import (getProjects, getDirs, writeProjects, writeDirs, loggedIn)


class Updater(QtCore.QRunnable):
    def __init__(self, _mode, do_debug=False, override=False):
        super(Updater, self).__init__()

        if not loggedIn():
            return self.signals.finished.emit('You must be logged in!')

        self.signals = UpdateSignals()
        self.threads = ["main"]
        self.workers = ["none"]
        self.current_count = 1
        self.debug_flag = 'corvid'
        if do_debug:
            self.debug_flag = + 'corvid-debug'

        if override:
            self.override_flag = '--override'
        else:
            self.override_flag = '--move'

        self.args = ['npx', self.debug_flag, 'pull', self.override_flag]

        if _mode == 'all':
            self.to_update = [p['abs_dir'] for p in getProjects()]
        elif _mode == 'stop':
            for worker in self.workers:
                worker.thread.stop()
        else:
            self.to_update = _mode

        try:
            for _p_ in range(thread_range):
                self.threads.append(QtCore.QThread())
                self.workers.append(UpdateWorker())
                self.workers[_p_].moveToThread(self.threads[_p_])
        except IndexError:
            print(len(self.to_update))

        self.iterate(self.current_count)

    def iterate(self, _ix_):
        try:
            is_done = self.workers[_ix_].startUpdate(
                self.to_update[_ix_], self.args)
        except AttributeError:
            self.loop(1)

        if _ix_ < len(self.to_update) - 1:
            is_done.npx_output.connect(self.loop)
        else:
            self.signals.finished.emit('success')

    def loop(self, exit_code):
        if exit_code != 0:
            self.signals.error.emit('error')
        self.signals.current.emit(self.to_update[self.current_count])
        self.current_count += 1
        self.iterate(self.current_count)
        self.signals.progress.emit(self.current_count, len(self.to_update))


class UpdateWorker(QtCore.QObject):
    npx_output = QtCore.pyqtSignal(int)

    @QtCore.pyqtSlot(int)
    def startUpdate(self, _path, args):
        try:
            now_updating = run(args, cwd=_path, capture_output=True)
            self.npx_output.emit(now_updating.check_returncode())
        except CalledProcessError:
            self.npx_output.emit(1)


class UpdateSignals(QtCore.QObject):
    progress = QtCore.pyqtSignal(int, int)
    finished = QtCore.pyqtSignal(str)
    current = QtCore.pyqtSignal(str)
    error = QtCore.pyqtSignal(str)


class FileWatcher(QtCore.QFileSystemWatcher, QtCore.QRunnable):
    def __init__(self):
        super(FileWatcher, self).__init__()
        self.watched_dirs = [p for p in getDirs().values()]
        self.addPaths(self.watched_dirs)
        self.signals = FileWatcherSignals()
        self.fileChanged.connect(self.handleFileChange)
        self.directoryChanged.connect(self.handleDirChange)

    def addWatched(self, _path):
        if isinstance(_path, str):
            self.addPath(_path)
            self.signals.success.emit()
        if isinstance(_path, list):
            self.addPaths(_path)
            self.signals.success.emit()
        self.signals.failure.emit(f'{_path} not valid type')

    def rmWatched(self, _path):
        if isinstance(_path, str):
            self.removePath(_path)
            self.signals.success.emit()
        if isinstance(_path, list):
            self.removePaths(_path)
            self.signals.success.emit()
        self.signals.failure.emit(f'{_path} not valid type')

    # def queryWatched(self, _pattern):
    #     self.signals.result.emit(
    #         [d for d in self.directories() if _pattern in d])

    # def queryInstanced(self, _path):
    #     _instance = [f for f in self.files() if f == _path][0]
    #     if not _instance:
    #         _closest = [f for f in self.files() if f in _path][0]
    #         self.signals.result.emit(_closest)
    #     self.signals.result.emit(_instance)

    def handleFileChange(self):
        writeProjects(self.files())
        self.signals.filechange.emit()

    def handleDirChange(self):
        writeDirs(self.directories())
        self.signals.dirchange.emit()


class FileWatcherSignals(QtCore.QObject):
    dirchange = QtCore.pyqtSignal()
    failure = QtCore.pyqtSignal(str)
    filechange = QtCore.pyqtSignal()
    # result = QtCore.pyqtSignal(list)
    success = QtCore.pyqtSignal()
