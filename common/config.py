import json


def load_ba_config(con):
    with open(config_filepath(con), 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def save_ba_config(con, data):
    with open(config_filepath(con), 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))


def config_filepath(con):
    return './configs/{0}.json'.format(con)


def config_dir():
    return './configs/'


def get_ss_path(self):
    return './runtime/ss_{0}.png'.format(self.con)
