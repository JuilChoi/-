from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

stul = 0
dchk = 0
k_csstr = 13.5
k_psstr = 11.5
k_pitr = 10.0
class MainApp(MDApp):
    def refresh_number_display(self):
        if self.root.ids.k_bs.text.replace(",", "").replace(".", "").isdigit():
            x = round(float(self.root.ids.k_bs.text.replace(",", "")), 0)
            self.root.ids.k_bs.text = f"{x:,.2f}"

        if self.root.ids.k_thp.text.replace(",", "").replace(".", "").isdigit():
            x = round(float(self.root.ids.k_thp.text.replace(",", "")), 0)
            self.root.ids.k_thp.text = f"{x:,.2f}"
            
    def core_calculation(self):
        self.checkbox = 0
        if self.root.ids.k_dchk == True:  
            self.checkbox = 1
        else:
            self.checkbox = 0
        
        self.d0 = float(self.root.ids.k_d01.text.replace(",", ""))
        self.d51 = float(self.root.ids.k_d02.text.replace(",", ""))
        self.d101 = float(self.root.ids.k_d03.text.replace(",", ""))
        self.d151 = float(self.root.ids.k_d04.text.replace(",", ""))
        self.d201 = float(self.root.ids.k_d05.text.replace(",", ""))
        self.d251 = float(self.root.ids.k_d06.text.replace(",", ""))
        self.d301 = float(self.root.ids.k_d07.text.replace(",", ""))

        # Calculate tax
        self.csst = round(self.bs / 100 * self.csstr, 2)
        if self.bs >= self.stul:
            self.psst = round(self.stul / 100 * self.psstr, 2)
        else:
            self.psst = round(self.bs / 100 * self.psstr, 2)
        self.psstd = round(self.bs - self.psst, 2)
        self.pit = round(self.psstd / 100 * self.pitr, 2)
        self.pitd = round(self.psstd - self.pit, 2)
        self.dis = 0

        chk = True
        if self.pit <= 20000:
            chk = False
            self.dis = self.pit

        if self.dchk == True:
            chk = False

        if chk == True:
            if self.psstd < 500_001:
                self.ids = self.d0
            elif self.psstd < 1_000_001:
                self.dis = self.d51
            elif self.psstd < 1_500_001:
                self.dis = self.d101
            elif self.psstd < 2_000_001:
                self.dis = self.d151
            elif self.psstd < 2_500_001:
                self.dis = self.d201
            elif self.psstd < 3_000_001:
                self.dis = self.d251
            else:
                self.dis = self.d301

    def calculate_basic_salary(self):
        self.csstr = float(k_csstr)
        self.psstr = float(k_psstr)
        self.pitr = float(k_pitr)
        self.stul = float(self.root.ids.k_stul.text.replace(",", ""))
        self.dchk = float(self.root.ids.k_dchk.active)
        self.bs = float(self.root.ids.k_bs.text.replace(",", ""))

        self.core_calculation()

        self.thp = round(self.pitd + self.dis, 2)
        self.root.ids.k_csst.text = f'{self.csst:,.2f}'
        self.root.ids.k_bs.text = f'{self.bs:,.2f}'
        self.root.ids.k_psst.text = f'{self.psst:,.2f}'
        self.root.ids.k_psstd.text = f'{self.psstd:,.2f}'
        self.root.ids.k_pit.text = f'{self.pit:,.2f}'
        self.root.ids.k_dis.text = f'{self.dis:,.2f}'
        self.root.ids.k_thp.text = f'{self.thp:,.2f}'

    def calculate_take_home_pay(self):
        # Set up variables for calculation
        self.csstr = float(k_csstr)
        self.psstr = float(k_psstr)
        self.pitr = float(k_pitr)
        self.stul = float(self.root.ids.k_stul.text.replace(",", ""))
        self.dchk = float(self.root.ids.k_dchk.active)
        self.thp = float(self.root.ids.k_thp.text.replace(",", ""))
        self.bs = round(self.thp * 1.5, 2)

        dif = 1
        while dif >= 0.5:
            self.core_calculation()
            cmp = round(self.pitd + self.dis, 2)
            dif = round(abs(cmp - self.thp), 2)
            self.bs = round(self.bs - dif, 0)
        self.root.thp = round(self.pitd + self.dis, 2)
        self.root.ids.k_csst.text = f"{self.csst:,.2f}"
        self.root.ids.k_bs.text = f"{self.bs:,.2f}"
        self.root.ids.k_psst.text = f"{self.psst:,.2f}"
        self.root.ids.k_psstd.text = f"{self.psstd:,.2f}"
        self.root.ids.k_pit.text = f"{self.pit:,.2f}"
        self.root.ids.k_dis.text = f"{self.dis:,.2f}"
        self.root.ids.k_thp.text = f"{self.thp:,.2f}"
    def build(self):                    
        kv = Builder.load_file('first_screen.kv')
        return kv

MainApp().run()


