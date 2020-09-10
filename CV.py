from pathlib import Path


class CV:
    def __init__(self, file: str):
        self.file = open(file).read()
        self.jobTitle = ""
        self.companyName = ""
        self.companyNameShort = ""
        self.companyAddr = ""
        self.companyProvince = ""
        self.receiver = ""
        self.receiverTitle = ""
        self.receiverLastName = ""

    def set_job(self, s):
        self.jobTitle = s

    def set_company_name(self, s):
        self.companyName = s  # Sap inc

    def set_company_name_short(self, s):
        self.companyNameShort = s  # SAP

    def set_company_addr(self, s):
        self.companyAddr = s

    def set_company_province(self, s):
        self.companyProvince = s

    def set_receiver(self, s):
        self.receiver = s

    def set_receiver_title(self, s):
        self.receiverTitle = s  # Mr.

    def set_receiver_last_name(self, s):
        self.receiverLastName = s

    def populate(self, target: str):
        self.file = self.file.replace('$JOB_TITLE$', self.jobTitle)
        self.file = self.file.replace('$COMPANY_NAME$', self.companyName)
        self.file = self.file.replace('$COMPANY_NAME_SHORT$', self.companyNameShort)
        self.file = self.file.replace('$COMPANY_ADDR$', self.companyAddr)
        self.file = self.file.replace('$COMPANY_ADDR_PROVINCE$', self.companyProvince)
        self.file = self.file.replace('$RECEIVER$', self.receiver)
        self.file = self.file.replace('$RECEIVER_TITLE$', self.receiverTitle)
        self.file = self.file.replace('$RECEIVER_LAST_NAME$', self.receiverLastName)
        out = open(target+'.tex', 'w')
        out.write(self.file)
        out.close()

