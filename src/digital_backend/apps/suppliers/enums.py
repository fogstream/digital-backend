class SupplierStatus:
    RESEARCH = 'RESEARCH'
    CLEAR = 'VALID'
    UNCLEAR = 'UNCLEAR'

    values = {
        RESEARCH: 'поиск информации',
        CLEAR: 'все в порядке',
        UNCLEAR: 'подозрительный клинет',
    }

    @classmethod
    def choices(cls):
        return cls.values.items()
