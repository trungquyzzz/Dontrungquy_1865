class SinhVien:
    def __init__(self, id, name, sex, major, diemtb):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemtb = diemtb
        self.hocluc = ""

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        self._major = value

    @property
    def diemtb(self):
        return self._diemtb

    @diemtb.setter
    def diemtb(self, value):
        self._diemtb = value

    def __str__(self):
        return "{:<5} {:<20} {:<10} {:<15} {:<10} {:<10}".format(self.id, self.name, self.sex, self.major, self.diemtb, self.hocluc)
