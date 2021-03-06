import copy
import json
import os
import platform
from datetime import datetime
from pathlib import Path
from subprocess import (run, CalledProcessError)


TERMINAL = {
    'Linux': 'gnome-terminal',
    'Windows': 'start powershell -WorkingDirectory',
    'Darwin': 'open -n /Applications/Utilities/Terminal.app'
}


def openInExplorer(_path_):
    _os_ = platform.system()

    try:
        if _os_ == 'Windows':
            run([os.path.join(os.getenv('WINDIR'), 'explorer.exe'),
                 '/select', os.path.normpath(_path_)])
        elif _os_ == 'Darwin':
            run(['open', _path_])
        elif _os_ == 'Linux':
            run(['xdg-open', _path_])

        return 'done'
    except CalledProcessError:
        return 'failed'


def projects():
    """morphing this into a function means it captures any and all changes to json"""
    with open('projects.json') as json_config:
        try:
            return json.load(json_config)
        except:
            return {'_init': 'false'}


def loggedIn():
    try:
        return projects()['logged_in'] != 'false'
    except KeyError:
        doInit()
        return loggedIn()


def dirScan(dir_to_scan):
    """10x faster parsing with ls -R over find!!"""
    found_files = [str(f)
                   for f in Path(dir_to_scan).rglob("*corvid-package.json")]

    corvid_files = []
    for _file_ in found_files:
        if not 'src/corvid-package.json' in _file_:
            continue
        project_loc = _file_.split('/src/corvid-package.json')[0]
        try:
            corvid_files.append({
                'abs_dir': project_loc,
                'slug': project_loc.split('/')[-1],
                'last_updated': datetime.now(),
                'due_date': 'none',
                'favorited': 'false'
            })
        except IndexError:
            print(_file_)
    return corvid_files


def subdirs(project_path):
    """this function will open only useful files in project directory in your editor of choice"""
    if not project_path.endswith('/'):
        project_path += '/'

    valid = {
        'pages': {'path': 'src/pages', 'type': 'js'},
        'backend': {'path': 'src/backend', 'type': 'any'},
        'public': {'path': 'src/public', 'type': 'any'},
        'lightboxes': {'path': 'src/lightboxes', 'type': 'js'}
    }

    def search(prop):
        _path_ = project_path + valid[prop]['path']
        to_open = Path(_path_).rglob("*")

        def check(_):
            if _.endswith('tsconfig.json') or _.endswith('authorization-config.json'):
                return False
            if valid[prop]['type'] == 'any':
                return True
            return valid[prop]['type'] == _.split('.')[-1]

        return [json.dumps(f'{_path_}/{_file_}') for _file_ in to_open if check(_file_)]

    return " ".join([search(_key_) for _key_ in {**valid}][0]) or None


def qzWrite(new_json):
    """rewrites json file with requested changes"""
    new_json['last_updated'] = datetime.now()
    with open('projects.json', 'w', encoding='utf-8') as current_json:
        json.dump(new_json, current_json,
                  ensure_ascii=False, indent=2, default=str, sort_keys=True)
        return 'done'


def isInt(n_o):
    """parseInt polyfill"""
    try:
        return int(n_o)
    except ValueError:
        return False


def isInit():
    """checks json to ensure existing install"""
    try:
        return projects()['_init'] and projects()['_init'] != 'false'
    except KeyError:
        doInit()
        return True


def getProjects():
    """current projects list"""
    try:
        return projects()['local_projects']
    except KeyError:
        doInit()
        return getProjects()


def writeProjects(new_projects):
    if not isinstance(new_projects, list):
        raise 'Not a valid projects format'

    try:
        re_write = clonedProjects()
        current_projects = getProjects()
        to_keep = [p for p in current_projects if p['abs_dir'] in new_projects]
        for _p_ in new_projects:
            if not _p_ in to_keep:
                to_keep.append({
                    'slug': _p_.split('/')[-1],
                    'abs_dir': _p_,
                    'last_updated': datetime.now(),
                    'favorited': 'false',
                    'due_date': 'none'
                })

        re_write['local_projects'] = to_keep
        qzWrite(re_write)
        return 'done'
    except:
        raise 'Uncaught error writing projects'


def getDirs():
    """current directories dictionary"""
    try:
        return projects()['_watched']
    except KeyError:
        doInit()
        return getDirs()


def writeDirs(new_dirs):
    if not isinstance(new_dirs, list):
        raise "Not a valid dirs format"

    try:
        re_write = clonedProjects()
        for new_dir in new_dirs:
            if new_dir == mainDir():
                re_write['main'] = new_dir
            else:
                new_key = new_dir.split('/')[-1]
                re_write['_watched'][new_key] = new_dir

        return 'done'
    except:
        raise 'Uncaught error writing dirs'


def clonedProjects():
    """clones json file for overwriting current"""
    return copy.deepcopy(projects())


def mainDir(new_dir=None):
    """sets or gets the main project directory
        sets if argument is passed
        gets if no argument"""
    if not new_dir:
        return getDirs()['main']

    qz_clone = clonedProjects()

    try:
        curr_key = [c for c in {**getDirs()} if c == new_dir][0]
        curr_path = getDirs()[curr_key]

        repl_key = qz_clone['_watched']['main'].split('/')[-1]
        qz_clone['_watched'][repl_key] = qz_clone['_watched']['main']

        del qz_clone['_watched'][curr_key]
        qz_clone['_watched']['main'] = curr_path
    except KeyError:
        raise 'Replacement failed'

    qzWrite(qz_clone)
    return 'done'


def doInit(refresh=False):
    """IMPORTANT: Changes made here must be made to rest of this script."""
    usr_home = str(Path.home())
    init_project = {
        '_init': 'yes',
        '_os': platform.system(),
        '_watched': {'main': usr_home},
        'last_updated': datetime.now(),
        'local_projects': dirScan(usr_home),
    }

    if not refresh:
        init_project['logged_in'] = 'false'
        init_project['_created'] = datetime.now()
        init_project['_config'] = {
            'update_on_start': 'false',
            'terminal': TERMINAL[platform.system()],
            'text_editor': 'none',
            'font': {'size': 'none', 'family': 'none'},
            'highlight_color': 'none'
        }
    else:
        init_project['logged_in'] = projects()['logged_in']
        init_project['_created'] = projects()['_created']
        init_project['_config'] = projects()['_config']

    qzWrite(init_project)
    return 'done'


def getByContext(context):
    """gets project by name or index and returns its full location path"""
    if context == '0':
        return getProjects()[0]['abs_dir']

    if isInt(context):
        return getProjects()[int(context)]['abs_dir']

    if not '/' in context:
        closest_match = ''

        for _ix_, _item_ in enumerate(getProjects()):
            if _item_['slug'] == context:
                return _item_['abs_dir']
            if _item_['slug'] in context:
                closest_match = _item_['abs_dir']
            if _ix_ == len(getProjects()) - 1 and closest_match != '':
                return closest_match
    else:
        return [_path_['abs_dir'] for _path_ in getProjects() if context in _path_['abs_dir']][0]

    return False


def withConfig(config=None):
    """sets or gets the config object"""
    if isInit():
        qz_clone = clonedProjects()
        if not config:
            return projects()['_config']
        if isinstance(config, str):
            try:
                return projects()['_config'][config]
            except:
                raise 'main.py: Not a valid key in config'
        if isinstance(config, dict):
            for _key_ in {**config}:
                qz_clone['_config'][_key_] = config[_key_]

            qzWrite(qz_clone)
            return qz_clone['_config']
        raise f'main.py: {config} not a valid parameter for config method'
    else:
        doInit()
        return withConfig(config)


def create(_dir_, _url_, do_debug=False):
    """
    clones a new project
    if auto is True, project editor is opened immediately upon creation
    """
    filtered = [o for o in getProjects() if o['abs_dir'] == _dir_]
    if len(filtered) > 0:
        raise 'Project already exists!'
    try:
        if (os.path.isdir(_dir_)):
            raise 'A project in that directory already exists!'

        Path(_dir_).mkdir(parents=True, exist_ok=True)

        if do_debug:
            do_exec = 'corvid-debug'
        else:
            do_exec = 'corvid'
        args = ['npx', do_exec, 'clone', _url_]
        npm_init = run(['npm', 'init', '-y'], cwd=_dir_)
        npm_init.check_returncode()

        if npm_init.stderr:
            print(npm_init.stderr)
        else:
            print(npm_init.stdout)

        npx_downloading = run(args, cwd=_dir_)
        npx_downloading.check_returncode()

        if npx_downloading.stderr:
            print(npx_downloading.stderr)
            raise f"""main.py: Error creating {_dir_}
{npx_downloading.stderr}"""

        if npx_downloading.stdout:
            print(npx_downloading.stdout)
            return 'done'
        return 'Invalid params'
    except CalledProcessError:
        raise f"""main.py: failed to create {_dir_}
{CalledProcessError}"""


def openByContext(_id_, do_debug=False, text_editor=False):
    """opens project by index or name"""
    try:
        curr_f = getByContext(_id_)

        if text_editor:
            usr_editor = withConfig('editor') or 'atom'
            found_files = subdirs(curr_f)
            if found_files:
                project_files = [usr_editor, *found_files]
            else:
                project_files = [usr_editor]

            text_editor = run(project_files)
            text_editor.check_returncode()

        debug_state = 'corvid'
        if do_debug:
            debug_state += '-debug'

        local_editor = run(
            ['npx', debug_state, 'open-editor'], cwd=curr_f)
        local_editor.check_returncode()

        return 'opening'
    except CalledProcessError:
        raise f"""main.py: Error opening {_id_}
{CalledProcessError}"""


def openInTerminal(_id_):
    """opens project directory in terminal emulator"""
    try:
        target_dir = getByContext(_id_)
        try:
            usr_emulator = withConfig('terminal')
        except KeyError:
            usr_emulator = TERMINAL[platform.system()]

        opening_terminal = run([usr_emulator], cwd=target_dir)
        opening_terminal.check_returncode()
        return True
    except CalledProcessError:
        raise f"""main.py: Error opening {_id_}
{CalledProcessError}"""


def appendProject(_id_):
    """writes an existing project to watch list --- does not clone"""
    qz_clone = clonedProjects()
    if getByContext(_id_.split('/')[-1]):
        return print('Project already exists!')
    try:
        new_project = {
            'abs_dir': _id_,
            'slug': _id_.split('/')[-1],
            'last_updated': datetime.now(),
            'due_date': 'none',
            'favorited': 'false'
        }
        qz_clone['local_projects'].append(new_project)
        qzWrite(qz_clone)
        return 'done!'
    except:
        raise f'main.py: Error while appending {_id_}'


def deleteProject(_id_):
    """deletes a watched project's entry in the [projects] array"""
    qz_clone = clonedProjects()
    to_delete = getByContext(_id_)
    to_write = []

    for _item_ in qz_clone['local_projects']:
        if _item_['abs_dir'] != to_delete:
            to_write.append(_item_)

    qz_clone['local_projects'] = to_write
    qzWrite(qz_clone)
    return 'done'


def getSnapshots(_id_):
    """returns an array of snapshot dirnames for given project"""
    curr_f = getByContext(_id_) + '/.corvid/snapshots'
    if not os.path.isdir(curr_f):
        raise f'main.py: {_id_} has no snapshots yet!'

    return [f for f in Path(curr_f).glob("*") if os.path.isdir(f)]


def toggleFavorite(_id_):
    """ability to tag projects as starred"""
    qz_clone = clonedProjects()
    focused_project = [px for px in getProjects(
    ) if px['abs_dir'] == getByContext(_id_)][0]

    focused_index = qz_clone['local_projects'].index(focused_project)

    is_favorited = focused_project['favorited']

    if is_favorited == 'true':
        qz_clone['local_projects'][focused_index]['favorited'] = 'false'
    else:
        qz_clone['local_projects'][focused_index]['favorited'] = 'true'
    qzWrite(qz_clone)
    return 'done'


def setDeadline(_id_, date_set):
    """adds or sets a project deadline"""
    qz_clone = clonedProjects()
    focused_project = [px for px in getProjects(
    ) if px['abs_dir'] == getByContext(_id_)][0]

    to_set = qz_clone['local_projects'].index(focused_project)

    if isinstance(date_set, str):
        qz_clone['local_projects'][to_set]['due_date'] = date_set
        qzWrite(qz_clone)
        return 'done'
    raise 'main.py: Not a valid date object'


def loginHandler():
    qz_clone = clonedProjects()
    try:

        login_attempt = run(["npx", "corvid", "login"], capture_output=True)

        if login_attempt.check_returncode() == 0:
            qz_clone['logged_in'] = 'true'
        else:
            qz_clone['logged_in'] = 'false'

    except CalledProcessError:
        qz_clone['logged_in'] = 'false'

    finally:
        qzWrite(qz_clone)


def logoutHandler():
    try:
        qz_clone = clonedProjects()

        logout_attempt = run(["npx", "corvid", "logout"], capture_output=True)
        if logout_attempt.check_returncode() == 0:
            qz_clone['logged_in'] = 'false'
        else:
            qz_clone['logged_in'] = 'true'

        qzWrite(qz_clone)
    except CalledProcessError:
        return "logout aborted"
