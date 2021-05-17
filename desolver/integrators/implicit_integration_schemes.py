import numpy

from .integrator_types import ImplicitRungeKuttaIntegrator
from .. import backend as D


class GaussLegendre4(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 4.0

    __alt_names__ = tuple()

    symplectic = True

    s = numpy.sqrt(3)

    tableau = numpy.array(
        [[0.5 - s / 6, 0.25, 0.25 - s / 6],
         [0.5 + s / 6, 0.25 + s / 6, 0.25]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, 0.5, 0.5]], dtype=numpy.float64
    )

    del s


class GaussLegendre6(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 6.0

    __alt_names__ = tuple()

    symplectic = True

    s = numpy.sqrt(15)

    tableau = numpy.array(
        [[0.5 - s / 10, 5 / 36, 2 / 9 - s / 15, 5 / 36 - s / 30],
         [0.5, 5 / 36 + s / 24, 2 / 9, 5 / 36 - s / 24],
         [0.5 + s / 10, 5 / 36 + s / 30, 2 / 9 + s / 15, 5 / 36]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, 5 / 18, 4 / 9, 5 / 18]], dtype=numpy.float64
    )

    del s


class LobattoIIIA2(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 2.0

    __alt_names__ = tuple()

    symplectic = False

    tableau = numpy.array(
        [[0, 0, 0],
         [1.0, 0.5, 0.5]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, 0.5, 0.5]], dtype=numpy.float64
    )


class LobattoIIIA4(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 4.0

    __alt_names__ = tuple()

    symplectic = False

    tableau = numpy.array(
        [[0.0, 0.0, 0.0, 0.0],
         [0.5, 5 / 24, 1 / 3, -1 / 24],
         [1.0, 1 / 6, 2 / 3, 1 / 6]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, 1 / 6, 2 / 3, 1 / 6]], dtype=numpy.float64
    )


class LobattoIIIB2(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 2.0

    __alt_names__ = tuple()

    symplectic = False

    tableau = numpy.array(
        [[0.5, 0.5, 0.0],
         [0.5, 0.5, 0.0]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, 0.5, 0.5]], dtype=numpy.float64
    )


class LobattoIIIB4(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 4.0

    __alt_names__ = tuple()

    symplectic = False

    tableau = numpy.array(
        [[0.0, 1 / 6, -1 / 6, 0.0],
         [0.5, 1 / 6, 1 / 3, 0.0],
         [1.0, 1 / 6, 5 / 6, 0.0]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, 1 / 6, 2 / 3, 1 / 6]], dtype=numpy.float64
    )


class LobattoIIIC2(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 2.0

    __alt_names__ = tuple()

    symplectic = False

    tableau = numpy.array(
        [[0.0, 0.5, -0.5],
         [1.0, 0.5, 0.5]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, 0.5, 0.5]], dtype=numpy.float64
    )


class LobattoIIIC4(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 4.0

    __alt_names__ = tuple()

    symplectic = False

    tableau = numpy.array(
        [[0.0, 1 / 6, -1 / 3, 1 / 6],
         [0.5, 1 / 6, 5 / 12, -1 / 12],
         [1.0, 1 / 6, 2 / 3, 1 / 6]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, 1 / 6, 2 / 3, 1 / 6],
         [0, -0.5, 2.0, -0.5]], dtype=numpy.float64
    )


class BackwardEuler(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 1.0

    __alt_names__ = tuple()

    symplectic = False

    tableau = numpy.array(
        [[1.0, 1.0]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, 1.0]], dtype=numpy.float64
    )


class ImplicitMidpoint(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 2.0

    __alt_names__ = tuple()

    symplectic = True

    tableau = numpy.array(
        [[0.5, 0.5]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, 1.0]], dtype=numpy.float64
    )


class CrankNicolson(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 2.0

    __alt_names__ = tuple()

    symplectic = False

    tableau = numpy.array(
        [[0.0, 0.0, 0.0],
         [1.0, 0.5, 0.5]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, 0.5, 0.5]], dtype=numpy.float64
    )


class DIRK3LStable(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 3.0

    __alt_names__ = tuple()

    symplectic = False

    tableau = numpy.array(
        [[0.5, 0.5, 0.0, 0.0, 0.0],
         [2.0 / 3.0, 1.0 / 6.0, 0.5, 0.0, 0.0],
         [0.5, -0.5, 0.5, 0.5, 0.0],
         [1.0, 1.5, -1.5, 0.5, 0.5]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, 1.5, -1.5, 0.5, 0.5]], dtype=numpy.float64
    )


class RadauIA3(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 3.0

    __alt_names__ = tuple()

    symplectic = False

    tableau = numpy.array(
        [[0.0, 1 / 4, -1 / 4],
         [2 / 3, 1 / 4, 5 / 12]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, 1 / 4, 3 / 4]], dtype=numpy.float64
    )


class RadauIA5(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 5.0

    __alt_names__ = tuple()

    symplectic = False

    s = numpy.sqrt(6)

    tableau = numpy.array(
        [[0.0, 1 / 9, (-1 - s) / 18, (-1 + s) / 18],
         [3 / 5 - s / 10, 1 / 9, 11 / 45 + 7 * s / 360, 11 / 45 - 43 * s / 360],
         [3 / 5 + s / 10, 1 / 9, 11 / 45 + 43 * s / 360, 11 / 45 - 7 * s / 360]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, 1 / 9, 4 / 9 + s / 36, 4 / 9 - s / 36]], dtype=numpy.float64
    )

    del s


class RadauIIA3(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 3.0

    __alt_names__ = tuple()

    symplectic = False

    tableau = numpy.array(
        [[1 / 3, 5 / 12, -1 / 12],
         [1, 3 / 4, 1 / 3]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, 3 / 4, 1 / 4]], dtype=numpy.float64
    )


class RadauIIA5(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 5.0

    __alt_names__ = tuple()

    symplectic = False

    s = numpy.sqrt(6)

    tableau = numpy.array(
        [[(4 - s) / 10, (88 - 7 * s) / 360, (296 - 169 * s) / 1800, (-2 + 3 * s) / 225],
         [(4 + s) / 10, (296 + 169 * s) / 1800, (88 + 7 * s) / 360, (-2 - 3 * s) / 225],
         [1, (16 - s) / 36, (16 + s) / 36, 1 / 9]], dtype=numpy.float64
    )

    final_state = numpy.array(
        [[0, (16 - s) / 36, (16 + s) / 36, 1 / 9],
         [0, 1 - 7 * s / 12, 1 + 7 * s / 12, -1]], dtype=numpy.float64
    )

    del s


class RadauIIA19(ImplicitRungeKuttaIntegrator):
    @property
    def order(self):
        return 19.0

    __alt_names__ = tuple()

    symplectic = False

    tableau = numpy.array([
        [
            0.014412409648876548632826740810813239411744731056578086070750679128,
            0.01847631341993400747592695722381535245022576145583384485927431185,
            -0.006980182933532836588678841759366987994474153027312215185589560855,
            0.005268407462093920382105416952948649531246096344101150697668426876,
            -0.004329902266726212297215732982619965881850640750699504718453469319,
            0.003664633468220373920396365335126456262678715789471125899010496399,
            -0.003121133313040942781794678870665443308910583427963636860467119166,
            0.002627238093136722861761357193605228380502683955424939626029261571,
            -0.002130727617625239684225999225208867577617558047969568567523547291,
            0.001563503775867901435140661113082336016873438305199311857327349538,
            -0.0006257404394511460905887641699035184669290295395073615365254704709],
        [
            0.074387389709196044635918185955998585080976913284735198426799602745,
            0.03971550605279189405510679648401445995284953871940635557084387294,
            0.04146594013277634914860000815671926802766316553895945899130432201,
            -0.01111550192186046711367752478853188294720954391125116082299584868,
            0.007632417536649012344703582281155378032554998632266435874572013793,
            -0.006010032538999333746999224183896838646016438738146769904679040784,
            0.004937965973404777678749925576855898927536077196358641619674709712,
            -0.004074782957950612690848195887267394998496209346894954423219673522,
            0.003267343698101428055591051631090540592769842293213388203242395546,
            -0.002382827468794315195497162549467827847547788339415961009550367788,
            0.0009513612030773121001889292353269839868732712402397643276072195226],
        [
            0.1761166561629952818631757460725685864113860479693058739346483371718,
            0.03546653596209324548953036182071435454111792378225085586594609870,
            0.08887784229548619086990692862983788566888839363163559806124591191,
            0.06067894120940990475345887027043103084497516731685925864609147990,
            -0.01415982900361989852898376438489565933401308573169972945023688873,
            0.009094640124757031592455679832762966013682754491594789406042620062,
            -0.006858410557171104203994878200302680694206709449262772176449878429,
            0.005417446351638549655293165203775295279096655006113010088995000597,
            -0.004241243344265243900605237054624704047404066162801510510301911286,
            0.003054235382056598968867284283211101475517929495493239186902821703,
            -0.001213502257389992832752664328341003336268914410876865183586917242],
        [
            0.3096675799276378170596204672294840488163890844971259245735924385418,
            0.03756910783964016930727028088688210375184385760439757506531628612,
            0.07901239141611847599154069794982713818155726789575047543661341043,
            0.1291326018252789289972577906556937386736705397861183748862308686,
            0.07420087910786776687201387182691293291316300488609859945245474554,
            -0.01597618013527057886172558694159493497284424163428731765151358547,
            0.009745034658284830104123689625342019875538300812371419153218756503,
            -0.007034700857040455095382812461888299749555856805881478810383650807,
            0.005264470305474794561997726821024536805275307152932972791939700821,
            -0.003705871655455991484803043493769231040893510520734293363677625270,
            0.001459847422739876667327852361054044378634415320359597613393532099],
        [
            0.4619704010810109348831431086805643081072330679787275209992998979929,
            0.03634354507157373122287271128472540681923113396196875878425719536,
            0.08399624348828787870508464381069998117489786396273158489512681502,
            0.1151507204422101744043991620408489361971201136907268722307952317,
            0.1564697706430008467251527416400316420735866981717359220851654324,
            0.08070546631213964884839142736889773855000315096628212589775026231,
            -0.01642014396964477658763571855839059439929425823757293695723775530,
            0.009566142530946837076251842658246031587030275224211389553481860032,
            -0.006547897285427787458570713067494797178997607683566049103644849506,
            0.004423063278304680883119352053441134896232548758374355712893801485,
            -0.001716509430380298935922340550441171612576850836164502099288095489],
        [
            0.6181172346952940246392297516035044802806674046397913475060393055586,
            0.03709667125719399823934056218624949145371583368000262203914529736,
            0.08110619387054557781210784335992823285225287408750422597711917812,
            0.1220424909922034122475239230528249091807510836984867395287482073,
            0.1403104983090434772518883056992371471992686747820998775398946974,
            0.1682152422057127108023554645025791965741042350452917113349657558,
            0.07955540810458212537726501760821651249044264911450915195149219713,
            -0.01545213709748905444929044648813174565970964169775047645037836043,
            0.008558328985579360169275700578770141399327163208985472279981681810,
            -0.005325894856198238015328752556460412817879677690407844435235507554,
            0.002010432924120655204092133660291007608394210411069867740306158540],
        [
            0.7628230151850396146826933071467255329235111827037380779911005908346,
            0.03663669374395105461814850680043364494050883722742823602520433578,
            0.08282053159803819450131846955509228450453677183982460161854002489,
            0.1182265658571560468938560082639338168090271404778501926089936682,
            0.1478684386806491755403291741194211163963265854635312127060929867,
            0.1520252053538656452473523140596265505587158409627786082743805945,
            0.1632188097396367535523409629362246637811476229442492696445043667,
            0.07086282453621987208805208535124840533718016052184161373215819494,
            -0.01314793051779103967268058787285478576093848083600435384889473724,
            0.006696949239695465571321212287088676338290732306225098603010042761,
            -0.002385073046381553657344838353488839981284028203986401372888886478],
        [
            0.88192102121000129980771488800526477630712058544870386191297665132831,
            0.03689958193203439368695382251979451977505679322735446001783271064,
            0.08185641384004000796739882957083379641266495133750185761842738464,
            0.1202983808099692707169222846863198884017508161495853265392899916,
            0.1440487144543105818936750789689878136009697772234180996062880701,
            0.1589346194973376746014568649679425410663939123646153851058655909,
            0.1491496171620095712625043262674279186165599192987159582290473452,
            0.1419615847228924548498665850195949882701529257469351926349617993,
            0.05547713807580017538798574249578457921834846344159161956296706093,
            -0.009643540890798499246829114514110387534117192917521947918721423655,
            0.002938511606405668687780468022689118479340219576507910517018121733],
        [
            0.9637421871167905390588356992319185479241288771581362138479503914356,
            0.03677365537640469013793882279844516853860980841359944315123131069,
            0.08231411145193487507150424527104696826001675891458522940763308846,
            0.1193331500935910704927628611479845191859928291457117771745056451,
            0.1457666870748447269812758835781235137414943213504235286292296241,
            0.1560344392637164542069129142646958259412914414366304657017135039,
            0.1541640183801730328658945885158311187774663548057418163107219969,
            0.1319693179612247424580813430119452774541904110163890453649803094,
            0.1064967726102315732267068276686411557742592361120693266069410591,
            0.03489287857495436057462180917165839069431426623170853743282321487,
            -0.004002843670284986956863596196453390443506550268722955931829361134],
        [
            1.000000000000000000000000000000000000000000000000000000000000000000,
            0.03680850274337924946552564703952257250633407560110190885784111690,
            0.08218800636846073785084083445387855020451656194507156599834064799,
            0.1195967158571898566882859830801363758258364741540254585528364764,
            0.1453050824164591555734315389815310253381621189272259396591735667,
            0.1567912286134691883479514236509898340189339712527769765855075256,
            0.1529296438622113105081377377003979801780786241826203904279240012,
            0.1340974189205893480292772376310295553451252092166458466844053840,
            0.1021350659395003377778943361115165106736257210286962005068043553,
            0.06014833527874081575865526135099759590938724369183571272716692583,
            0.010000000000000000000000000000000000000000000000000000000000000000]
    ], dtype=numpy.float64)

    final_state = numpy.array([
        [1.0,
         0.03680850274337924946552564703952257250633407560110190885784111690,
         0.08218800636846073785084083445387855020451656194507156599834064799,
         0.1195967158571898566882859830801363758258364741540254585528364764,
         0.1453050824164591555734315389815310253381621189272259396591735667,
         0.1567912286134691883479514236509898340189339712527769765855075256,
         0.1529296438622113105081377377003979801780786241826203904279240012,
         0.1340974189205893480292772376310295553451252092166458466844053840,
         0.1021350659395003377778943361115165106736257210286962005068043553,
         0.06014833527874081575865526135099759590938724369183571272716692583,
         0.010000000000000000000000000000000000000000000000000000000000000000],
        [1.0,
         0.000111677695713657757062698891880706843728654156750323672093847952,
         -0.000374789055929833804794037217207453893530096760223574238193409412,
         0.0006820145757646047502809102002793308989941358728074423799166826524,
         -0.0009706622643735461546458098299827473890710310580707658350230239825,
         0.00119367247245614804601066322573572560166761645552917586186173174719,
         -0.0013192871745202003341119720339385000469624189162389242743609897010,
         0.00132964434372530388245970367166906172190048190748045984144621431750,
         -0.0012146959224468732879762022162956221166730438181317487188418946093,
         0.00095624732961073914571404530785949837994570216009761131110084104535,
         -0.0003938220000000000000000000000000000000000000000000000000000000000
         ]
    ], dtype=numpy.float64)

    def get_error_estimate(self):
        if self.adaptive:
            return D.sum(self.final_state[1][self.tableau_idx_expand] * self.aux, axis=0)
        else:
            return D.zeros_like(self.dState)

    def update_timestep(self, initial_state, dState, diff, initial_time, timestep, tol=0.8):
        err_estimate = D.max(D.abs(D.to_float(diff)))
        relerr = D.max(D.to_float(self.atol + self.rtol * D.abs(initial_state) + self.rtol * D.abs(dState / timestep)))
        corr = 1.0
        if err_estimate != 0:
            corr = corr * tol * (relerr / err_estimate) ** (1.0 / 10.0)
        if corr != 0:
            timestep = corr * timestep
        if err_estimate > relerr:
            return timestep, True
        else:
            return timestep, False
