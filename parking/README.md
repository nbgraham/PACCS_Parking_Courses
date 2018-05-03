# OU Parking Data Machine Learning

## Not Relevant anymore
Overall, this project was deemed not necesary. Parking usage is fairly consistent week to week, so there is no need for a machine learning model to predict it.

## Data
All the [input data](input_data) has been mostly removed for data security. Only a few entries have been preserved to show the data format. The cleaned_data folder has been removed, but those can be generated from the input_dat with parse_enrollment.py and parse_parking.py.

## Models
### Linear Regression
Coefficients are strongly affected by the range of values. Need to scale inputs
```
Boyd House
[('year', 132229823971.1202), ('fall', 56305133869.38306), ('Archeological Survey BuildingBEFORE', 11315832900.94985), ('825 Research ParkwayBEFORE', 8093978535.554328), ('Ceramics StudioBEFORE', 5554066061.477728), ('Copeland HallBEFORE', 4057300854.8682165), ('Carpenter HallBEFORE', 3724864295.2466364), ('College of Allied HealthNOW', 3197091665.6648426), ('Burton HallBEFORE', 2782536176.474293), ('Burton HallAFTER', 2717138937.729496)]
0.9063304849912649
Duck Pond
[('lot_capacity', 5117391512937.327), ('year', 2475790015140.6406), ('fall', 1210279822346.3044), ('Adams Center DormBEFORE', 168396092425.87656), ('Archeological Survey BuildingBEFORE', 106970345205.38756), ('Buchanan HallBEFORE', 101847373151.36598), ('Farzaneh HallBEFORE', 98361713375.25635), ('Cate Center OneNOW', 86625462316.30197), ('College of Allied HealthNOW', 83076479654.70132), ('Kaufman HallNOW', 78226638636.09125)]
0.8940212257038008
Jenkins
[('lot_capacity', 235071433531.07663), ('Buchanan HallBEFORE', 25055242214.28301), ('College of Allied HealthNOW', 14033292577.497128), ('Adams Center DormBEFORE', 13245245005.4713), ('Three Partners PlaceAFTER', 12587621037.982407), ('Richards Hall AddNOW', 12536343861.406797), ('Fred Jones Art MuseumNOW', 12426598268.598972), ('Moore Public SchoolsAFTER', 11574787535.31901), ('Academic CenterBEFORE', 10853620754.21499), ('Lawton MacArthur High SchoolNOW', 10408913367.605509)]
0.8594777675238837
Monett Lot - North
[('year', 24631703290.804066), ('655 Research ParkwayBEFORE', 5381633082.647291), ('825 Research ParkwayBEFORE', 2473278422.7608657), ('Main Building - TexomaBEFORE', 1421504824.4753847), ('Bizzell LibraryBEFORE', 1377748739.5183814), ('Stephenson Life Sci ResearchAFTER', 1289831411.6521573), ('Carnegie BuildingBEFORE', 1204812557.2782845), ('Lissa and Cy Wagner HallNOW', 1197497697.9806461), ('Headington Residential CollegeBEFORE', 1133936201.5767167), ('Farzaneh HallBEFORE', 1129640548.185218)]
0.9204571882562838
```

### Random Forest
```
Boyd House
[('Dale HallNOW', 0.6297731869489364), ('no_school', 0.09168689472448398), ('Felgar HallNOW', 0.0675602248363418), ('SJ Sarkeys ComplexNOW', 0.05093130499865049), ('days_into_semester', 0.03015203981562927), ('home_gameday', 0.02223713295005511), ('Gaylord HallNOW', 0.013013878982151736), ('Cate Center OneAFTER', 0.010743081136205182), ('hour', 0.009262736653613294), ('Physical Science CtrNOW', 0.006863597962931024)]
0.9482649694806797
Duck Pond
[('Felgar HallNOW', 0.4611516370627841), ('no_school', 0.08926635690444608), ('SJ Sarkeys ComplexBEFORE', 0.07773994417400627), ('Sarkeys Energy CtrNOW', 0.07010707543141893), ('Kaufman HallNOW', 0.06366579262011571), ('Sarkeys Energy CtrBEFORE', 0.05113810837791997), ('days_into_semester', 0.039893789923031574), ('home_gameday', 0.022607483136810023), ('Cross Center AAFTER', 0.01625968537106164), ('SJ Sarkeys ComplexAFTER', 0.012031416516963399)]
0.9410981636395791
Jenkins
[('Sarkeys Energy CtrNOW', 0.30021766395941596), ('Copeland HallNOW', 0.2234188367812721), ('Felgar HallNOW', 0.15233279065575495), ('no_school', 0.10165476733235561), ('Dale HallNOW', 0.07444047641659271), ('Law CenterNOW', 0.03455287638278107), ('days_into_semester', 0.02178687856817633), ('Cate Center OneAFTER', 0.016079356546413077), ('Kaufman HallAFTER', 0.01557719614924571), ('home_gameday', 0.00750597390937448)]
0.8850810269045987
Monett Lot - North
[('Sarkeys Energy CtrNOW', 0.23132470674402414), ('Physical Science CtrNOW', 0.20832730420290718), ('no_school', 0.12596938616145364), ('Kaufman HallAFTER', 0.08999485573849834), ('Felgar HallNOW', 0.07376939028252404), ('SJ Sarkeys ComplexNOW', 0.0732686699155095), ('Copeland HallNOW', 0.06764021504370996), ('days_into_semester', 0.029481539690595537), ('Catlett Music CtrNOW', 0.014808376755657295), ('Felgar HallAFTER', 0.01015286141635451)]
0.9372269411007269
```


**!!!!!! Column names below here are sketchy !!!!!!**
## Comparing data

### Actual validation
- Lot index, lot capacity, weekday_index, hour, current_enrollment
```
Boyd House
[('Copeland Hall', 0.7286976255813243), ('Carson Engr Ctr', 0.08049787095737918), ('Robertson Hall', 0.04310213213196918), ('Sam Noble OK Museum Nat Hist', 0.021717963896314172), ('Law Center', 0.01940949802546383), ('Collums Building', 0.01690145252061592), ('lot_capacity', 0.008335765627044323), ('Fredrick Douglass Center', 0.006921597426492805), ('Carnegie Building', 0.006659885017361161), ('Radar Innovations Lab', 0.004203714511249133)]
0.7260161036199968
Duck Pond
[('Farzaneh Hall', 0.39373919984708144), ('Carpenter Hall', 0.1704891158243785), ('SJ Sarkeys Complex', 0.15710183479240966), ('Academic Center', 0.07923960872338937), ('Sam Noble OK Museum Nat Hist', 0.021664668294462095), ('Robertson Hall', 0.01531162118150416), ('lot_capacity', 0.014786059533296652), ('Headington Hall', 0.014672755967194712), ('N.C. Bldg 210', 0.013136397205996065), ('Catlett Music Ctr', 0.008422847691120294)]
0.8008489135864267
Jenkins
[('SJ Sarkeys Complex', 0.34987404708319286), ('Collums Building', 0.24742123638064067), ('Copeland Hall', 0.16969590954561872), ('Old Faculty Club', 0.08571439161202088), ('Intramural Soccer Field', 0.03619573356961304), ('lot_capacity', 0.011459755352340211), ('Cate Center Two', 0.010294211432651622), ('Carnegie Building', 0.009019580440358013), ('Fred Jones Art Museum', 0.006259898748051333), ('N.C. Bldg 101', 0.005279489828624801)]
0.7027756801051037
Monett Lot - North
[('SJ Sarkeys Complex', 0.5956424171084266), ('Carnegie Building', 0.15954815186731588), ('Fears Structural Engr Lab', 0.08020344341119293), ('Cate Center Two', 0.05063445261619061), ('lot_capacity', 0.014267115196813429), ('Fredrick Douglass Center', 0.009337821662899627), ('Law Center', 0.008540077715316056), ('Lawton Eisenhower High School', 0.005679033020257598), ('Fine Arts Center', 0.00541135238867859), ('Chemistry Building', 0.005411216098280236)]
0.6629569337955616
```
- Lot index, lot capacity, weekday_index, hour, **no_school**, **home_gameday**, current_enrollment
```
Boyd House
[('Copeland Hall', 0.42638814567544037), ('SJ Sarkeys Complex', 0.2856090567026253), ('weekday_index', 0.12211999438514118), ('Robertson Hall', 0.03824677651431367), ('hour', 0.03484828305299077), ('lot_capacity', 0.02153050931633911), ('Collums Building', 0.019837340391024978), ('Archeological Survey Building', 0.007985787722666896), ('Fredrick Douglass Center', 0.007131278108940981), ('Radar Innovations Lab', 0.004607375722722306)]
0.88594742790366
Duck Pond
[('Farzaneh Hall', 0.34045357180457786), ('Huston Huffman Center', 0.14871078857652548), ('SJ Sarkeys Complex', 0.14092020738025673), ('weekday_index', 0.10630712020877967), ('Academic Center', 0.06892243088696771), ('Headington Hall', 0.03899809190824989), ('hour', 0.02513982401409237), ('lot_capacity', 0.020618121835424573), ('Robertson Hall', 0.019278491644135167), ('Cross Center A', 0.016839650585262152)]
0.9296774636974214
Jenkins
[('SJ Sarkeys Complex', 0.5371801372575071), ('Old Faculty Club', 0.14616604007210987), ('weekday_index', 0.13027750778770927), ('Copeland Hall', 0.07406772272760735), ('Robertson Hall', 0.03190569299210733), ('Cate Center Two', 0.023884324971064123), ('Intramural Soccer Field', 0.012741143650442191), ('lot_capacity', 0.01205771841072898), ('hour', 0.004516884224870567), ('Academic Center', 0.003078067576982354)]
0.915627317648011
Monett Lot - North
[('SJ Sarkeys Complex', 0.26263543273918544), ('Carnegie Building', 0.2259453753540365), ('Archeological Survey Building', 0.1556566913849463), ('Farzaneh Hall', 0.1479246150749032), ('weekday_index', 0.11552045622917377), ('Robertson Hall', 0.024166145558832758), ('Cate Center Two', 0.01371309578668399), ('hour', 0.0108611425244313), ('lot_capacity', 0.005279752147131741), ('College of Allied Health', 0.004745884849555744)]
0.9177934084904966
```
- Lot index, lot capacity, **fall**, **spring**, weekday_index, hour, **no_school**, **home_gameday**, current_enrollment
```
Boyd House
[('Copeland Hall', 0.6535152625166327), ('weekday_index', 0.11389321993675057), ('Collums Building', 0.09005758274645863), ('Robertson Hall', 0.048595043841799454), ('hour', 0.0307072602413092), ('spring', 0.010897709048005218), ('SJ Sarkeys Complex', 0.00694059905342289), ('Farzaneh Hall', 0.005745164425532994), ('Archeological Survey Building', 0.0048261311897893865), ('N.C. Bldg 210', 0.004315069852469319)]
0.9039045422781729
Duck Pond
[('Farzaneh Hall', 0.5061740795158649), ('weekday_index', 0.08283122433151036), ('SJ Sarkeys Complex', 0.07425716962502896), ('Carpenter Hall', 0.07300072769581625), ('Academic Center', 0.07290154496714131), ('Headington Hall', 0.040761849203485974), ('Robertson Hall', 0.025752562650187726), ('hour', 0.02287642139976523), ('spring', 0.013379069578158976), ('N.C. Bldg 210', 0.009528600426824916)]
0.8958706167152255
Jenkins
[('Collums Building', 0.38481835620555294), ('Copeland Hall', 0.14336595323261594), ('weekday_index', 0.11392671946712767), ('SJ Sarkeys Complex', 0.07834760461617465), ('Academic Center', 0.077409731591214), ('Old Faculty Club', 0.07151162858115531), ('Robertson Hall', 0.038655710577270276), ('Cate Center Two', 0.019803255768340765), ('Fredrick Douglass Center', 0.015051208800601245), ('spring', 0.009425251790626369)]
0.8952683796603977
Monett Lot - North
[('SJ Sarkeys Complex', 0.46556958111735786), ('Old Faculty Club', 0.14502335886012124), ('weekday_index', 0.1377323728717928), ('Collums Building', 0.07559244888606971), ('Carnegie Building', 0.07270594788710182), ('Cate Center Two', 0.03433494784598909), ('Robertson Hall', 0.0222433328140472), ('hour', 0.011031159386925438), ('spring', 0.006792256554036704), ('Comp Wind Tunnel', 0.006615372785472247)]
0.8959083095670975
```

- Lot index, lot capacity, weekday_index, hour, **no_school**, **home_gameday**, **prev_enrollment**, current_enrollment, **next_enrollment**
```
Boyd House
[('Copeland HallNOW', 0.5678843730653457), ('Collums BuildingNOW', 0.14431861955700856), ('weekday_index', 0.11110287176684823), ('hour', 0.03508964111673445), ('Robertson HallNOW', 0.03063686027686654), ('Robertson HallAFTER', 0.01744481314342264), ('N.C. Bldg 210NOW', 0.00970263446283661), ('Fears Structural Engr LabNOW', 0.007157025887099215), ('Fredrick Douglass CenterNOW', 0.006746180465183047), ('Oklahoma Memorial StadiumBEFORE', 0.005742193478131738)]
0.9407274646454753
Duck Pond
[('Farzaneh HallNOW', 0.2193373577889483), ('Academic CenterNOW', 0.20990392831506757), ('Carpenter HallNOW', 0.13514014254948242), ('weekday_index', 0.08510066645552372), ('Huston Huffman CenterNOW', 0.0727274505128952), ('SJ Sarkeys ComplexNOW', 0.06840611874744625), ('Oklahoma Memorial StadiumBEFORE', 0.032016042142598525), ('hour', 0.02763386144000976), ('Carpenter HallAFTER', 0.024281426919326374), ('Copeland HallBEFORE', 0.01834383243778296)]
0.9219696425532306
Jenkins
[('Collums BuildingNOW', 0.3683197589592323), ('Dale HallBEFORE', 0.14757625320141027), ('weekday_index', 0.1360831028178553), ('Carnegie BuildingNOW', 0.08045577451584077), ('SJ Sarkeys ComplexNOW', 0.07546612119046564), ('Copeland HallNOW', 0.06896994010197696), ('Huston Huffman CenterAFTER', 0.02493670965895709), ('SJ Sarkeys ComplexAFTER', 0.013874397871113936), ('Cate Center TwoNOW', 0.013160993315961189), ('Farzaneh HallAFTER', 0.012198954616990661)]
0.8323116345648932
Monett Lot - North
[('SJ Sarkeys ComplexNOW', 0.3145641375154482), ('weekday_index', 0.1276056590684172), ('Old Faculty ClubNOW', 0.07915822578978324), ('Huston Huffman CenterNOW', 0.07739640620672206), ('Copeland HallNOW', 0.07613816291067098), ('Farzaneh HallNOW', 0.07499282996318643), ('Fears Structural Engr LabNOW', 0.07314146878727378), ('Carnegie BuildingNOW', 0.0708255055296032), ('Cate Center TwoNOW', 0.019994643201717337), ('hour', 0.009464835173729109)]
0.9139147659479214
```
- Lot index, lot capacity, weekday_index, hour, **days_into_semester**, **no_school**, **home_gameday**, current_enrollment
```
Boyd House
[('SJ Sarkeys Complex', 0.3708263783118143), ('Copeland Hall', 0.2910039703278623), ('Collums Building', 0.10088138111699183), ('hour', 0.0841509364466571), ('Robertson Hall', 0.036245053940156334), ('days_into_semester', 0.028701472437144472), ('weekday_index', 0.025480066874455427), ('lot_capacity', 0.01572439291681116), ('Huston Huffman Center', 0.008792806664588695), ('N.C. Bldg 210', 0.0058622594736510445)]
0.9272854998803451
Duck Pond
[('Farzaneh Hall', 0.564750676457001), ('hour', 0.08128170532072121), ('Collums Building', 0.07104381447435344), ('Academic Center', 0.06792156358608474), ('Headington Hall', 0.04064326022713433), ('weekday_index', 0.0339034542480338), ('Robertson Hall', 0.025754016198802344), ('N.C. Bldg 210', 0.023992413696692316), ('days_into_semester', 0.013652595251958943), ('lot_capacity', 0.005500413873740402)]
0.8872400930135415
Jenkins
[('Old Faculty Club', 0.4244050357859613), ('SJ Sarkeys Complex', 0.14946719662732583), ('hour', 0.14413255823323667), ('Collums Building', 0.06884103930399278), ('Farzaneh Hall', 0.06341162442504168), ('Robertson Hall', 0.042109431612313016), ('weekday_index', 0.02829494965375216), ('Intramural Soccer Field', 0.020059683512424254), ('Cate Center Two', 0.014672185015310386), ('lot_capacity', 0.0069538032931467375)]
0.9202322950666326
Monett Lot - North
[('Old Faculty Club', 0.2977676940698825), ('Fears Structural Engr Lab', 0.20864790558948898), ('SJ Sarkeys Complex', 0.11870314256406618), ('hour', 0.10108960992771246), ('Robertson Hall', 0.08086235038558534), ('Collums Building', 0.0751313960451764), ('weekday_index', 0.02555159214356888), ('Cate Center Two', 0.019657706746687494), ('Copeland Hall', 0.010269673058366383), ('days_into_semester', 0.008514951933437345)]
0.9426916995847656
```
- Lot index, lot capacity, weekday_index, hour, **days_into_semester**, **no_school**, **home_gameday**, **prev_enrollment**, current_enrollment, **next_enrollment**
```
Boyd House
[('Copeland HallNOW', 0.34283511211141926), ('SJ Sarkeys ComplexNOW', 0.2092480022546869), ('Farzaneh HallNOW', 0.13653124827683413), ('hour', 0.11982673040971481), ('Robertson HallNOW', 0.032079211720572445), ('days_into_semester', 0.029309316653845684), ('weekday_index', 0.0277410488485982), ('Fredrick Douglass CenterNOW', 0.027412543161370262), ('Oklahoma Memorial StadiumBEFORE', 0.007786174714976948), ('Intramural Soccer FieldBEFORE', 0.00772063902244817)]
0.9169931387177213
Duck Pond
[('Farzaneh HallNOW', 0.34072274829968163), ('Collums BuildingNOW', 0.1277651996083002), ('hour', 0.08175295136502327), ('Academic CenterNOW', 0.07195773956003268), ('Carpenter HallNOW', 0.06888790890484818), ('Huston Huffman CenterNOW', 0.06579283292482344), ('weekday_index', 0.03558406350909232), ('SJ Sarkeys ComplexBEFORE', 0.02469047493672493), ('Oklahoma Memorial StadiumBEFORE', 0.024581054256973257), ('days_into_semester', 0.02310603070305396)]
0.9178609274828726
Jenkins
[('SJ Sarkeys ComplexNOW', 0.3666613223998873), ('Old Faculty ClubNOW', 0.21289671931460755), ('hour', 0.12589349357819263), ('Copeland HallNOW', 0.07479547513812092), ('Fred Jones Art MuseumNOW', 0.0671601411786856), ('weekday_index', 0.027549795233583578), ('Intramural Soccer FieldNOW', 0.026383936262730695), ('Robertson HallNOW', 0.025815892944890832), ('SJ Sarkeys ComplexAFTER', 0.009083379400434157), ('lot_capacity', 0.00687470112479707)]
0.9342738889042145
Monett Lot - North
[('Robertson HallNOW', 0.2771701994132509), ('Cate Center TwoNOW', 0.207518625420968), ('Carnegie BuildingNOW', 0.15084148229519925), ('hour', 0.13987347649291673), ('Fredrick Douglass CenterNOW', 0.07201701665647056), ('SJ Sarkeys ComplexNOW', 0.056313135796089486), ('weekday_index', 0.026634107512178363), ('SJ Sarkeys ComplexAFTER', 0.009916882399453885), ('days_into_semester', 0.009903599443373701), ('N.C. Bldg 210NOW', 0.005945310754060027)]
0.8938043349971065
```

### On self (fall and spring)
- Lot index, lot capacity, weekday_index, hour, current_enrollment
```
0.828374855321128
[('Copeland Hall', 0.4067376066425214), ('Collums Building', 0.17665612352851168), ('SJ Sarkeys Complex', 0.17280711084396977), ('Farzaneh Hall', 0.08263367064801967), ('lot_capacity', 0.03735532959197694), ('Robertson Hall', 0.025271576491369917), ('Law Center', 0.01931805746391147), ('Huston Huffman Center', 0.010706083563569765), ('Fredrick Douglass Center', 0.006435089108677803), ('Carnegie Building', 0.0054210611657751085)]
0.8321457163517885
[('Farzaneh Hall', 0.47660701743673994), ('Academic Center', 0.16265261680879906), ('Huston Huffman Center', 0.07921926068345986), ('Collums Building', 0.07900067578208653), ('Robertson Hall', 0.02442534482627429), ('Sam Noble OK Museum Nat Hist', 0.019851697843213178), ('Headington Hall', 0.019295950680568504), ('lot_capacity', 0.01679743760024894), ('Law Center', 0.009001697927559203), ('Archeological Survey Building', 0.007603944037120644)]
0.8200409144694762
[('SJ Sarkeys Complex', 0.5953110744683379), ('Collums Building', 0.0834415931494458), ('Farzaneh Hall', 0.0832598067727239), ('Academic Center', 0.08039541868966105), ('Cate Center Two', 0.030782973473763842), ('Intramural Soccer Field', 0.026774179696557144), ('Robertson Hall', 0.012765536202769587), ('Burton Hall', 0.007971244693973829), ('lot_capacity', 0.00762796268000498), ('Sam Noble OK Museum Nat Hist', 0.007158519231021938)]
0.822433779636519
[('SJ Sarkeys Complex', 0.5255110229202785), ('Old Faculty Club', 0.15912846346609097), ('Carnegie Building', 0.08411862934029316), ('Farzaneh Hall', 0.08139059824753953), ('Cate Center Two', 0.050817512120021516), ('Robertson Hall', 0.013064468877859791), ('lot_capacity', 0.012543649440680902), ('Law Center', 0.009947401258023526), ('Rawls Engr Practice Facility', 0.005949529294123701), ('Fred Jones Art Museum', 0.0043624192754185016)]
```
- Lot index, lot capacity, weekday_index, hour, **no_school**, **home_gameday**, current_enrollment
```
0.9514923350312985
[('Copeland Hall', 0.43296939716953514), ('SJ Sarkeys Complex', 0.21568860227382008), ('weekday_index', 0.11371728829624231), ('Farzaneh Hall', 0.07738837972059787), ('Robertson Hall', 0.05039082983257905), ('hour', 0.030796419083454523), ('Collums Building', 0.01573249733817831), ('lot_capacity', 0.014740979608912482), ('Fredrick Douglass Center', 0.012293663362954559), ('Radar Innovations Lab', 0.004927923330870919)]
0.9373840753560035
[('Farzaneh Hall', 0.49870364697971975), ('weekday_index', 0.08645326810688156), ('Collums Building', 0.07634016171713023), ('Academic Center', 0.07381989390980291), ('SJ Sarkeys Complex', 0.07219481489518026), ('Headington Hall', 0.04158210315670423), ('Robertson Hall', 0.030014213253129324), ('hour', 0.02454631579233645), ('lot_capacity', 0.016438239172814513), ('N.C. Bldg 210', 0.014207228029247187)]
0.9490642176905631
[('SJ Sarkeys Complex', 0.5294767626363042), ('weekday_index', 0.140921287714621), ('Fred Jones Art Museum', 0.07653606202822921), ('Collums Building', 0.07300731500466359), ('Old Faculty Club', 0.07039301969935866), ('Robertson Hall', 0.03595098112908759), ('Cate Center Two', 0.01567137469565926), ('Intramural Soccer Field', 0.014455161662321673), ('lot_capacity', 0.009023713604849833), ('Chemistry Building', 0.004623070093719451)]
0.9482041752413887
[('SJ Sarkeys Complex', 0.5351884908799607), ('Huston Huffman Center', 0.14141802962173206), ('weekday_index', 0.13513881182698467), ('Collums Building', 0.07350599974785889), ('Cate Center Two', 0.04657118851843915), ('hour', 0.013878990383427348), ('Robertson Hall', 0.007591891514660826), ('Intramural Soccer Field', 0.007217020487216228), ('lot_capacity', 0.006151242077820265), ('N.C. Bldg 101', 0.004624127839731864)]
```
- Lot index, lot capacity, weekday_index, hour, no_school, home_gameday, **prev_enrollment**, current_enrollment, **next_enrollment**
```
0.9515933715447704
[('Copeland HallNOW', 0.4263254850859382), ('SJ Sarkeys ComplexNOW', 0.14327748397125828), ('weekday_index', 0.11555591440780877), ('Collums BuildingNOW', 0.07871386812626784), ('Farzaneh HallNOW', 0.07805152813859981), ('hour', 0.03140400912451741), ('Robertson HallNOW', 0.025432536815864215), ('lot_capacity', 0.011836889701412568), ('Carpenter HallAFTER', 0.010025503416112243), ('Oklahoma Memorial StadiumBEFORE', 0.008586409975087264)]
0.9375537164714
[('Farzaneh HallNOW', 0.5629019412968245), ('weekday_index', 0.08763696295036424), ('Huston Huffman CenterNOW', 0.07537680064166695), ('Academic CenterNOW', 0.07289021325683759), ('SJ Sarkeys ComplexBEFORE', 0.025011804184335757), ('Sam Noble OK Museum Nat HistBEFORE', 0.023057415630137152), ('hour', 0.02280195992901388), ('Oklahoma Memorial StadiumBEFORE', 0.014515140587863105), ('Robertson HallBEFORE', 0.008825873760646731), ('Carpenter HallAFTER', 0.007121806974689948)]
0.9496238605136118
[('SJ Sarkeys ComplexNOW', 0.3679111364097545), ('Collums BuildingNOW', 0.2209162428616885), ('weekday_index', 0.13041609534663484), ('Farzaneh HallNOW', 0.07561957274032556), ('Old Faculty ClubNOW', 0.07334212654578674), ('Robertson HallNOW', 0.02380147181274447), ('Intramural Soccer FieldNOW', 0.01971072569055886), ('Cate Center TwoNOW', 0.014545049106711557), ('Carpenter HallAFTER', 0.012919706917935304), ('Cate Center TwoAFTER', 0.008429348714484464)]
0.947903358073628
[('SJ Sarkeys ComplexNOW', 0.606580775910148), ('weekday_index', 0.13446754919586873), ('Collums BuildingAFTER', 0.079741632702403), ('Collums BuildingNOW', 0.07738544604902271), ('Cate Center TwoNOW', 0.0326057452005788), ('hour', 0.009849586737171212), ('Huston Huffman CenterAFTER', 0.009144190184728998), ('Farzaneh HallAFTER', 0.005208016554765292), ('lot_capacity', 0.005191857019342662), ('Robertson HallNOW', 0.00417142807406626)]
```
- Lot index, lot capacity, weekday_index, hour, **days_into_semester**, no_school, home_gameday, current_enrollment
```
0.9872587214823308
[('Copeland Hall', 0.6216748823594047), ('hour', 0.11578376061025537), ('SJ Sarkeys Complex', 0.07572300226428175), ('Robertson Hall', 0.049616933969610685), ('weekday_index', 0.03064562987366424), ('days_into_semester', 0.024211939831630856), ('Collums Building', 0.016638492537497922), ('lot_capacity', 0.010362406338190243), ('N.C. Bldg 210', 0.00620167356021723), ('Farzaneh Hall', 0.004442283124591052)]
0.9838859582291708
[('Farzaneh Hall', 0.48123136719141124), ('hour', 0.08304209808732096), ('Academic Center', 0.0727406801969068), ('SJ Sarkeys Complex', 0.06798417855145411), ('Huston Huffman Center', 0.06788470101579877), ('weekday_index', 0.039712308847882447), ('Headington Hall', 0.025408173659823514), ('days_into_semester', 0.024671063984056146), ('Robertson Hall', 0.02456775721135948), ('Sam Noble OK Museum Nat Hist', 0.013234410299736519)]
0.985316456051052
[('Collums Building', 0.3397584509446613), ('SJ Sarkeys Complex', 0.22727280289701052), ('hour', 0.13521109296704145), ('Farzaneh Hall', 0.0732421372143788), ('Old Faculty Club', 0.07125207574202749), ('Cate Center Two', 0.04025892769835353), ('weekday_index', 0.030532257607233503), ('Robertson Hall', 0.026663892128951684), ('lot_capacity', 0.009474312248411056), ('Comp Wind Tunnel', 0.005735069544729087)]
0.9867476063078258
[('SJ Sarkeys Complex', 0.456056376337418), ('hour', 0.12644168695638364), ('Robertson Hall', 0.0823230976139818), ('Old Faculty Club', 0.06989771041695207), ('Collums Building', 0.06952595721857878), ('Carnegie Building', 0.06804820398427916), ('weekday_index', 0.03434207285587659), ('Cate Center Two', 0.033289251371162974), ('days_into_semester', 0.009990647248643885), ('Fredrick Douglass Center', 0.006861520220962465)]
```
- Lot index, lot capacity, weekday_index, hour, **days_into_semester**, no_school, home_gameday, **prev_enrollment**, current_enrollment, **next_enrollment**
```
0.9884014896976576
[('Copeland HallNOW', 0.4885477892481845), ('SJ Sarkeys ComplexNOW', 0.14152021740568227), ('hour', 0.11278452182287961), ('Farzaneh HallNOW', 0.06796688628044299), ('Robertson HallNOW', 0.04211433349786618), ('weekday_index', 0.027572221576685558), ('days_into_semester', 0.023156360550461313), ('Collums BuildingNOW', 0.020046393080403558), ('N.C. Bldg 210NOW', 0.008158949404084723), ('lot_capacity', 0.007120077426232557)]
0.9838685461475225
[('Farzaneh HallNOW', 0.4764977362781032), ('Academic CenterNOW', 0.20048745778086743), ('hour', 0.09176394326496785), ('weekday_index', 0.036029016354190854), ('SJ Sarkeys ComplexBEFORE', 0.024607152479354973), ('days_into_semester', 0.01984541265480553), ('Oklahoma Memorial StadiumBEFORE', 0.017299428010420743), ('Sam Noble OK Museum Nat HistBEFORE', 0.014000903263634379), ('Carpenter HallAFTER', 0.013953937544687007), ('Comp Wind TunnelAFTER', 0.008966087108244791)]
0.9862436397362
[('Collums BuildingNOW', 0.4239944461915062), ('SJ Sarkeys ComplexNOW', 0.21552126340378538), ('hour', 0.13009160804985065), ('Old Faculty ClubNOW', 0.07251131606653308), ('weekday_index', 0.028938223577595318), ('Intramural Soccer FieldNOW', 0.01757161823582263), ('Carpenter HallAFTER', 0.015985157799269324), ('Huston Huffman CenterAFTER', 0.013726601421755214), ('Robertson HallNOW', 0.013604551457851444), ('Cate Center TwoNOW', 0.010397192690051385)]
0.9862650264844849
[('SJ Sarkeys ComplexNOW', 0.37160808531254713), ('Fears Structural Engr LabNOW', 0.13885351652514766), ('hour', 0.1364450781401197), ('Carnegie BuildingNOW', 0.07245134308009632), ('Old Faculty ClubNOW', 0.0702822403054392), ('Collums BuildingNOW', 0.06879628307353738), ('weekday_index', 0.030598376026138834), ('Cate Center TwoNOW', 0.018127196172681683), ('Huston Huffman CenterAFTER', 0.014906546187802234), ('days_into_semester', 0.014041459707531057)]
```
