from django.contrib import admin

from pyconcz_2017.proposals.admin import EntryAdmin


class Proposals:
    configs = {}

    def register(self, config):
        self.configs[config.key] = config

    def get_config(self, key):
        return self.configs[key]


proposals = Proposals()
