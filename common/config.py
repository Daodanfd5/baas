import json
from modules.daily import arena, cafe, wanted, special_entrust, shop, schedule, make, group, buy_ap
from modules.reward import mailbox, momo_talk, work_task
from modules.scan import hard_task, normal_task
from modules.activity import tutor_dept
from modules.baas import restart, cm, setting


def load_ba_config(con):
    with open(config_filepath(con), 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def save_ba_config(con, data):
    with open(config_filepath(con), 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False, sort_keys=False))


def config_filepath(con):
    return './configs/{0}.json'.format(con)


def config_dir():
    return './configs/'


def get_ss_path(self):
    return './runtime/ss_{0}.png'.format(self.con)


def get_render(con):
    bc = load_ba_config(con)
    data = {
        'baas': setting.render,
        'restart': restart.render,
        'arena': arena.render,
        'cafe': cafe.render,
        'group': group.render,
        'make': make.render,
        'schedule': schedule.render,
        'shop': shop.render,
        'special_entrust': special_entrust.render,
        'wanted': wanted.render,
        'mailbox': mailbox.render,
        'momo_talk': momo_talk.render,
        'work_task': work_task.render,
        'hard_task': hard_task.render,
        'normal_task': normal_task.render,
        'tutor_dept': tutor_dept.render,
        'buy_ap': buy_ap.render,
    }
    cr = cm.render
    for task, task_config in bc.items():
        if task not in data:
            continue
        for fn, module in task_config.items():
            if fn != 'base':
                continue
            for field, value in module.items():
                key = "{0}.{1}".format(fn, field)
                if key in cr:
                    data[task][key] = cr[key]
    return data
