"""
ophyd commands from SPEC config file

from file: /home/beams/IXS/spec/config/herix/config

CAUTION: Review the object names below before using them!
    Some names may not be valid python identifiers
    or may be reserved (such as ``time`` or ``del``)
    or may be vulnerable to re-definition because
    they are short or common.
"""

# __all__ = """
# """.split()

from ..session_logs import logger

logger.info(__file__)


from ophyd import EpicsMotor, EpicsSignal
from ophyd.scaler import ScalerCH

wbsvb = EpicsMotor("30ida:m1", name="wbsvb", labels=("motor",))  # WBSlitV_B
wbshr = EpicsMotor("30ida:m2", name="wbshr", labels=("motor",))  # WBSlitH_R
wbsvt = EpicsMotor("30ida:m3", name="wbsvt", labels=("motor",))  # WBSlitV_T
wbshl = EpicsMotor("30ida:m4", name="wbshl", labels=("motor",))  # WBSlitH_L
crly = EpicsMotor("30ida:m5", name="crly", labels=("motor",))  # CRL_Y
crlx = EpicsMotor("30ida:m6", name="crlx", labels=("motor",))  # CRL_X
bim1 = EpicsMotor("30ida:m7", name="bim1", labels=("motor",))  # BIM1_X
crlax = EpicsMotor("30ida:m8", name="crlax", labels=("motor",))  # CRL_AX
hhlmth = EpicsMotor("30ida:m9", name="hhlmth", labels=("motor",))  # HHLMTheta
hhlmy1 = EpicsMotor("30ida:m10", name="hhlmy1", labels=("motor",))  # HHLM_Y1
hhlmz2 = EpicsMotor("30ida:m11", name="hhlmz2", labels=("motor",))  # HHLM_Z2
hhlmth2 = EpicsMotor("30ida:m12", name="hhlmth2", labels=("motor",))  # HHLMTheta2
hhlmx2 = EpicsMotor("30ida:m13", name="hhlmx2", labels=("motor",))  # HHLM_X2
hhlmch2 = EpicsMotor("30ida:m14", name="hhlmch2", labels=("motor",))  # HHLM_Chi2
hhlmxt = EpicsMotor("30ida:m15", name="hhlmxt", labels=("motor",))  # HHLM_XT
hhlmyt = EpicsMotor("30ida:m16", name="hhlmyt", labels=("motor",))  # HHLM_YT
bslvd = EpicsMotor("30ida:m17", name="bslvd", labels=("motor",))  # BSlitV-DW
bslvu = EpicsMotor("30ida:m18", name="bslvu", labels=("motor",))  # BSlitV-UP
bslho = EpicsMotor("30ida:m19", name="bslho", labels=("motor",))  # BSlitH-Out
bslhi = EpicsMotor("30ida:m20", name="bslhi", labels=("motor",))  # BSlitH-In
secth = EpicsMotor("30ida:m57", name="secth", labels=("motor",))
secy = EpicsMotor("30ida:m62", name="secy", labels=("motor",))
secx = EpicsMotor("30ida:m60", name="secx", labels=("motor",))
crlay = EpicsMotor("30ida:m21", name="crlay", labels=("motor",))  # CRL_AY
# Macro Motor: SpecMotor(mne='wbsvg', config_line='24', macro_prefix='wbsSoftV') # read_mode=7
# Macro Motor: SpecMotor(mne='wbsvc', config_line='25', macro_prefix='wbsSoftV') # read_mode=7
# Macro Motor: SpecMotor(mne='wbshg', config_line='26', macro_prefix='wbsSoftH') # read_mode=7
# Macro Motor: SpecMotor(mne='wbshc', config_line='27', macro_prefix='wbsSoftH') # read_mode=7
# Macro Motor: SpecMotor(mne='bslvg', config_line='28', macro_prefix='bslSoftV') # read_mode=7
# Macro Motor: SpecMotor(mne='bslvc', config_line='29', macro_prefix='bslSoftV') # read_mode=7
# Macro Motor: SpecMotor(mne='bslhg', config_line='30', macro_prefix='bslSoftH') # read_mode=7
# Macro Motor: SpecMotor(mne='bslhc', config_line='31', macro_prefix='bslSoftH') # read_mode=7
# Macro Motor: SpecMotor(mne='kohzuE', config_line='32', name='KohzuE', macro_prefix='kohzuE')  # KohzuE # read_mode=7
hrmx1 = EpicsMotor("30ida:m33", name="hrmx1", labels=("motor",))  # HRM_X1
hrmx2 = EpicsMotor("30ida:m34", name="hrmx2", labels=("motor",))  # HRM_X2
hrmx3 = EpicsMotor("30ida:m35", name="hrmx3", labels=("motor",))  # HRM_X3
hrmth1 = EpicsMotor("30ida:m36", name="hrmth1", labels=("motor",))  # HRM_th1
hrmth2 = EpicsMotor("30ida:m37", name="hrmth2", labels=("motor",))  # HRM_th2
hrmth3 = EpicsMotor("30ida:m38", name="hrmth3", labels=("motor",))  # HRM_th3
hrmy1 = EpicsMotor("30ida:m39", name="hrmy1", labels=("motor",))  # HRM_y1
hrmy2 = EpicsMotor("30ida:m40", name="hrmy2", labels=("motor",))  # HRM_y2
hrmy3 = EpicsMotor("30ida:m41", name="hrmy3", labels=("motor",))  # HRM_y3
hrmtil1 = EpicsMotor("30ida:m42", name="hrmtil1", labels=("motor",))  # HRM_tilt1
hrmtil3 = EpicsMotor("30ida:m43", name="hrmtil3", labels=("motor",))  # HRM_tilt3
hmmini1 = EpicsMotor("30ida:m46", name="hmmini1", labels=("motor",))  # HRM_Mini1
hmmini2 = EpicsMotor("30ida:m47", name="hmmini2", labels=("motor",))  # HRM_Mini2
s2th = EpicsMotor("30idc:m25", name="s2th", labels=("motor",))
th = EpicsMotor("30idc:m26", name="th", labels=("motor",))
chi = EpicsMotor("30idc:m27", name="chi", labels=("motor",))
phi = EpicsMotor("30idc:m28", name="phi", labels=("motor",))
cam_x = EpicsMotor("30idc:m29", name="cam_x", labels=("motor",))  # cam-x
cam_y = EpicsMotor("30idc:m22", name="cam_y", labels=("motor",))  # cam-y
cam_z = EpicsMotor("30idc:m31", name="cam_z", labels=("motor",))  # focus
atten = EpicsMotor("30idc:m32", name="atten", labels=("motor",))
stbly = EpicsMotor("30idc:m16", name="stbly", labels=("motor",))
stblx = EpicsMotor("30idc:m21", name="stblx", labels=("motor",))
stblz = EpicsMotor("30idc:m23", name="stblz", labels=("motor",))
slity = EpicsMotor("30idc:m58", name="slity", labels=("motor",))
slitx = EpicsMotor("30idc:m57", name="slitx", labels=("motor",))
cam_ax = EpicsMotor("30idc:m64", name="cam_ax", labels=("motor",))  # cam_AX
xu = EpicsMotor("30idc:m9", name="xu", labels=("motor",))
zu = EpicsMotor("30idc:m10", name="zu", labels=("motor",))
yu = EpicsMotor("30idc:m11", name="yu", labels=("motor",))
xd = EpicsMotor("30idc:m12", name="xd", labels=("motor",))
yd = EpicsMotor("30idc:m13", name="yd", labels=("motor",))
tth = EpicsMotor("30idc:Herix_theta", name="tth", labels=("motor",))  # HerixTTH
hx = EpicsMotor("30idc:Herix_x", name="hx", labels=("motor",))  # HerixX
hy = EpicsMotor("30idc:Herix_y", name="hy", labels=("motor",))  # HerixY
hz = EpicsMotor("30idc:Herix_z", name="hz", labels=("motor",))  # HerixZ
hax = EpicsMotor("30idc:Herix_ax", name="hax", labels=("motor",))  # HerixAX
hay = EpicsMotor("30idc:Herix_ay", name="hay", labels=("motor",))  # HerixAY
herixE = EpicsMotor("30idc:SM13", name="herixE", labels=("motor",))  # HerixE
a1ax = EpicsMotor("30idc:m39", name="a1ax", labels=("motor",))
a1ay = EpicsMotor("30idc:m40", name="a1ay", labels=("motor",))
a2ax = EpicsMotor("30idc:m41", name="a2ax", labels=("motor",))
a2ay = EpicsMotor("30idc:m42", name="a2ay", labels=("motor",))
a3ax = EpicsMotor("30idc:m43", name="a3ax", labels=("motor",))
a3ay = EpicsMotor("30idc:m44", name="a3ay", labels=("motor",))
a4ax = EpicsMotor("30idc:m45", name="a4ax", labels=("motor",))
a4ay = EpicsMotor("30idc:m46", name="a4ay", labels=("motor",))
a5ax = EpicsMotor("30idc:m47", name="a5ax", labels=("motor",))
a5ay = EpicsMotor("30idc:m48", name="a5ay", labels=("motor",))
a6ax = EpicsMotor("30idc:m49", name="a6ax", labels=("motor",))
a6ay = EpicsMotor("30idc:m50", name="a6ay", labels=("motor",))
a7ax = EpicsMotor("30idc:m51", name="a7ax", labels=("motor",))
a7ay = EpicsMotor("30idc:m52", name="a7ay", labels=("motor",))
a8ax = EpicsMotor("30idc:m53", name="a8ax", labels=("motor",))
a8ay = EpicsMotor("30idc:m54", name="a8ay", labels=("motor",))
a9ax = EpicsMotor("30idc:m55", name="a9ax", labels=("motor",))
a9ay = EpicsMotor("30idc:m56", name="a9ay", labels=("motor",))
cslvd = EpicsMotor("30idc:m17", name="cslvd", labels=("motor",))  # cslit_vd
cslvu = EpicsMotor("30idc:m18", name="cslvu", labels=("motor",))  # cslit_vu
cslho = EpicsMotor("30idc:m20", name="cslho", labels=("motor",))  # cslit_ho
cslhi = EpicsMotor("30idc:m19", name="cslhi", labels=("motor",))  # cslit_hi
micro_y = EpicsMotor("30idc:m36", name="micro_y", labels=("motor",))
micro_x = EpicsMotor("30idc:m37", name="micro_x", labels=("motor",))
rbs_xy = EpicsMotor("30idc:m30", name="rbs_xy", labels=("motor",))
micro_z = EpicsMotor("30idc:m38", name="micro_z", labels=("motor",))
# Macro Motor: SpecMotor(mne='cslvg', config_line='98', macro_prefix='cslSoftV') # read_mode=7
# Macro Motor: SpecMotor(mne='cslvc', config_line='99', macro_prefix='cslSoftV') # read_mode=7
# Macro Motor: SpecMotor(mne='cslhg', config_line='100', macro_prefix='cslSoftH') # read_mode=7
# Macro Motor: SpecMotor(mne='cslhc', config_line='101', macro_prefix='cslSoftH') # read_mode=7
# Macro Motor: SpecMotor(mne='hpzt1', config_line='102', name='HM_PZT1', macro_prefix='PI516')  # HM_PZT1 # read_mode=7
# Macro Motor: SpecMotor(mne='hpzt2', config_line='103', name='HM_PZT2', macro_prefix='PI516')  # HM_PZT2 # read_mode=7
# Macro Motor: SpecMotor(mne='hpzt3', config_line='104', name='HM_PZT3', macro_prefix='PI516')  # HM_PZT3 # read_mode=7
# Macro Motor: SpecMotor(mne='pzt', config_line='105', macro_prefix='pzt') # read_mode=7
# 106: MOT106 =    NONE:0/0   2000  1  2000  200   50  125    0 0x003   mot169  Motor 169  # Motor 169
b2vup = EpicsMotor("30ida:m58", name="b2vup", labels=("motor",))
b2vdown = EpicsMotor("30ida:m59", name="b2vdown", labels=("motor",))
# 109: MOT109 =    NONE:0/0   2000  1  2000  200   50  125    0 0x003   mot172  Motor 172  # Motor 172
b2hin = EpicsMotor("30ida:m61", name="b2hin", labels=("motor",))
# 111: MOT111 =    NONE:0/0   2000  1  2000  200   50  125    0 0x003   mot174  Motor 174  # Motor 174
b2hout = EpicsMotor("30ida:m63", name="b2hout", labels=("motor",))
# 113: MOT113 =    NONE:0/0   2000  1  2000  200   50  125    0 0x003   mot176  Motor 176  # Motor 176
# Macro Motor: SpecMotor(mne='b2slvg', config_line='114', macro_prefix='b2SoftV') # read_mode=0
# Macro Motor: SpecMotor(mne='b2slvc', config_line='115', macro_prefix='b2SoftV') # read_mode=0
# Macro Motor: SpecMotor(mne='b2slhg', config_line='116', macro_prefix='b2SoftH') # read_mode=0
# Macro Motor: SpecMotor(mne='b2slhc', config_line='117', macro_prefix='b2SoftH') # read_mode=0
sl_ana5 = EpicsMotor("30idc:m59", name="sl_ana5", labels=("motor",))  # Slit ana5 # read_mode=0
pin_an5 = EpicsMotor("30idd:m3", name="pin_an5", labels=("motor",))  # PIN ana5 # read_mode=0
fpd_x = EpicsMotor("30idd:m4", name="fpd_x", labels=("motor",))  # FPD X # read_mode=0
zoom = EpicsMotor("30idc:m4", name="zoom", labels=("motor",))  # Zoom Cam # read_mode=0
cam_ay = EpicsMotor("30idc:m24", name="cam_ay", labels=("motor",))  # cam_AY # read_mode=0
ruby_x = EpicsMotor("30idd:m1", name="ruby_x", labels=("motor",))  # Ruby_X # read_mode=0
nrsE = EpicsMotor("30idc:SM18", name="nrsE", labels=("motor",))  # NRSE
hrmic2y = EpicsMotor("30ida:m68", name="hrmic2y", labels=("motor",))  # HRM IC2 Y
hrmic3y = EpicsMotor("30ida:m69", name="hrmic3y", labels=("motor",))  # HRM IC3 Y
ana5_d = EpicsMotor("30idc:SM20", name="ana5_d", labels=("motor",))  # Anal5 Diam
th_b = EpicsMotor("30idb:m20", name="th_b", labels=("motor",))  # sample_th_b
mxb = EpicsMotor("30idb:m17", name="mxb", labels=("motor",))  # micro_x_b
myb = EpicsMotor("30idb:m18", name="myb", labels=("motor",))  # micro_y_b
mzb = EpicsMotor("30idb:m19", name="mzb", labels=("motor",))  # micro_z_b
cxb = EpicsMotor("30idb:m23", name="cxb", labels=("motor",))  # clean_up_x_b
cyb = EpicsMotor("30idb:m24", name="cyb", labels=("motor",))  # clean_up_y_b
x_b = EpicsMotor("30idb:m25", name="x_b", labels=("motor",))  # sample_x_b
y_b = EpicsMotor("30idb:m26", name="y_b", labels=("motor",))  # sample_y_b
z_b = EpicsMotor("30idb:m27", name="z_b", labels=("motor",))  # sample_z_b
phi_b = EpicsMotor("30idb:m28", name="phi_b", labels=("motor",))  # sample_Phi_b
ana5_f = EpicsMotor("30idd:m13", name="ana5_f", labels=("motor",))  # Ana5_Focus # read_mode=0
ana9_d = EpicsMotor("30idd:m12", name="ana9_d", labels=("motor",))  # Anal9 Diam # read_mode=0
ana7_d = EpicsMotor("30idd:m11", name="ana7_d", labels=("motor",))  # Anal7_Diam # read_mode=0
ana3_d = EpicsMotor("30idd:m10", name="ana3_d", labels=("motor",))  # Anal3_Diam # read_mode=0
ana1_d = EpicsMotor("30idd:m9", name="ana1_d", labels=("motor",))  # Anal1 Diam # read_mode=0
btablex = EpicsMotor("30idb:SM7", name="btablex", labels=("motor",))
btabley = EpicsMotor("30idb:SM10", name="btabley", labels=("motor",))
btablez = EpicsMotor("30idb:SM9", name="btablez", labels=("motor",))
bsherix = EpicsMotor("30idd:m14", name="bsherix", labels=("motor",))  # Beam_Stop_Herix
phply = EpicsMotor("30ida:m25", name="phply", labels=("motor",))
phplx = EpicsMotor("30ida:m26", name="phplx", labels=("motor",))
# 149: MOT149 =  ANC300:0/1   2000  1  2000  200   10  125    0 0x003     anc1  anc1
# 150: MOT150 =  ANC300:0/2   2000  1  2000  200   10  125    0 0x003     anc2  anc2
phplth = EpicsMotor("30ida:SM1", name="phplth", labels=("motor",))  # read_mode=7
geth = EpicsMotor("30ida:m27", name="geth", labels=("motor",))  # Ge_th
dummy = EpicsMotor("30idd:m16", name="dummy", labels=("motor",))  # Dummymotor
phplthc = EpicsMotor("30ida:m72", name="phplthc", labels=("motor",))  # phplth_c
anaaux = EpicsMotor("30idd:m5", name="anaaux", labels=("motor",))  # Analyzer_Aux
hrmic1y = EpicsMotor("30ida:m67", name="hrmic1y", labels=("motor",))  # HRM IC1 Y
hrmic1x = EpicsMotor("30ida:m22", name="hrmic1x", labels=("motor",))  # HRM IC1 X
hrmic2x = EpicsMotor("30ida:m23", name="hrmic2x", labels=("motor",))  # HRM IC2 X
hrmic3x = EpicsMotor("30ida:m24", name="hrmic3x", labels=("motor",))  # HRM IC3 X
ana9_sl = EpicsMotor("30idd:m13", name="ana9_sl", labels=("motor",))  # ana9_slit_blades


scaler1 = ScalerCH("30idb:scaler1", name="scaler1", labels=("detectors",))
scaler1.select_channels(None)
sec = scaler1.channels.chan01.s
hmic1 = scaler1.channels.chan03.s
hmic2 = scaler1.channels.chan04.s
pinb = scaler1.channels.chan06.s
hmic3 = scaler1.channels.chan05.s
hmic0 = scaler1.channels.chan02.s
apd4 = scaler1.channels.chan12.s
oldana8 = EpicsSignal("30idc:scaler1.S3", name="oldana8", labels=("detectors",))  # OldAna8
oldana6 = EpicsSignal("30idc:scaler1.S5", name="oldana6", labels=("detectors",))  # OldAna6
oldana4 = EpicsSignal("30idc:scaler1.S7", name="oldana4", labels=("detectors",))  # OldAna4
oldana2 = EpicsSignal("30idc:scaler1.S11", name="oldana2", labels=("detectors",))  # OldAna2
icoc = EpicsSignal("30idc:scaler1.S13", name="icoc", labels=("detectors",))  # ICO-C
pind = EpicsSignal("30idc:scaler1.S14", name="pind", labels=("detectors",))  # PIN-D
pinc = EpicsSignal("30idc:scaler1.S15", name="pinc", labels=("detectors",))  # PIN-C
ip = EpicsSignal("30idc:scaler2.S9", name="ip", labels=("detectors",))  # IN-P
id = EpicsSignal("30idc:scaler2.S10", name="id", labels=("detectors",))  # IN-D
fp = scaler1.channels.chan09.s
fd = scaler1.channels.chan10.s
dr0 = EpicsSignal("tmm:pv.VAL", name="dr0", labels=("detectors",))  # det-r0
apdb = scaler1.channels.chan11.s
hstemp1 = EpicsSignal("30idct:D1Ch1_calc.VAL", name="hstemp1", labels=("detectors",))  # Heat Stage T1
hstemp2 = EpicsSignal("30idct:D1Ch2_calc.VAL", name="hstemp2", labels=("detectors",))  # Heat Stage T2
hstemp3 = EpicsSignal("30idct:D1Ch3_calc.VAL", name="hstemp3", labels=("detectors",))  # Heat Stage T3
ampv = scaler1.channels.chan07.s
amph = scaler1.channels.chan08.s
ana1 = EpicsSignal("s30_pilatus1:ROIStat1:1:Total_RBV", name="ana1", labels=("detectors",))  # Ana1
ana2 = EpicsSignal("s30_pilatus1:ROIStat1:6:Total_RBV", name="ana2", labels=("detectors",))  # Ana2
ana3 = EpicsSignal("s30_pilatus1:ROIStat1:2:Total_RBV", name="ana3", labels=("detectors",))  # Ana3
ana4 = EpicsSignal("s30_pilatus1:ROIStat1:7:Total_RBV", name="ana4", labels=("detectors",))  # Ana4
ana5 = EpicsSignal("s30_pilatus1:ROIStat1:3:Total_RBV", name="ana5", labels=("detectors",))  # Ana5
ana6 = EpicsSignal("s30_pilatus1:ROIStat1:8:Total_RBV", name="ana6", labels=("detectors",))  # Ana6
ana7 = EpicsSignal("s30_pilatus1:ROIStat1:4:Total_RBV", name="ana7", labels=("detectors",))  # Ana7
ana8 = EpicsSignal("s30_pilatus1:ROIStat1:9:Total_RBV", name="ana8", labels=("detectors",))  # Ana8
ana9 = EpicsSignal("s30_pilatus1:ROIStat1:5:Total_RBV", name="ana9", labels=("detectors",))  # Ana9
