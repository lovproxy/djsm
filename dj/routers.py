class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'dj':
            if model._meta.model_name == 'xd':
                return 'xd.db'
            elif model._meta.model_name == 'xd2':
                return 'xd2.db'
            elif model._meta.model_name == 'xd3':
                return 'xd3.db'
            elif model._meta.model_name == 'xd4':
                return 'xd4.db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'dj':
            if model._meta.model_name == 'xd':
                return 'xd.db'
            elif model._meta.model_name == 'xd2':
                return 'xd2.db'
            elif model._meta.model_name == 'xd3':
                return 'xd3.db'
            elif model._meta.model_name == 'xd4':
                return 'xd4.db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'dj':
            if model_name == 'xd':
                return db == 'xd.db'
            elif model_name == 'xd2':
                return db == 'xd2.db'
            elif model_name == 'xd3':
                return db == 'xd3.db'
            elif model_name == 'xd4':
                return db == 'xd4.db'
            return db == 'default'
        return True 