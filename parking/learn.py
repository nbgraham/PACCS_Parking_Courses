import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from matplotlib import pyplot as plt
from datetime import datetime
from sklearn.metrics import mean_squared_error
from math import sqrt

np.random.seed(42)


spring_2017= {
    'start': datetime(2017, 8, 21)
    'end': datetime(2017,12, 15)
}
fall_2018 = {
    'start': datetime(2018, 1, 16),
    'end': datetime(2018, 5, 12)
}
semesters = [spring_2017, fall_2018]
def in_session(datetime_str):
    date = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
    for sem in semesters:
        if sem['start'] <= date <= sem['end']:
            return True
    return False


def get_data(columns=None, ignore_neg_occupancy=True, ignore_breaks=True):
    data = pd.read_csv('cleaned_data/parking_enrollment.pd')

    if ignore_breaks:
        data = data[list(map(in_session, data['datetime']))]

    if ignore_neg_occupancy:
        data = data[data['occ'] >= 0]

    if columns is not None:
        remove_columns = []
        for col in data.columns:
            if col not in columns:
                remove_columns.append(col)

        data = data.drop(columns=remove_columns)

    return data


def train_test_split(df, train_p=0.8):
    train_i = []
    test_i = []
    steps = 4
    step_size = len(df) // steps
    train_n = int(step_size * train_p)
    for i in range(4):
        rf = np.random.permutation(step_size)
        rf += i * step_size

        train_i.extend(rf[:train_n])
        test_i.extend(rf[train_n:])

    train = df.iloc[train_i]
    test = df.iloc[test_i]

    return train, test


def x_y(df):
    df = df.drop(columns=['datetime','weekday','occ_type'])
    X_df = df.drop(columns=['occ'])
    X_cols = X_df.columns
    X = X_df.values
    y = df['occ'].values
    return X_cols, X, y


def main():
    lot_info = ['lot', 'capacity', 'occ_type', 'weekday']
    date_info = ['datetime', 'year', 'fall', 'spring', 'days_into_semester', 'weekday_index', 'hour', 'no_school', 'home_gameday']
    enroll_before = ['655 Research ParkwayBEFORE', '825 Research ParkwayBEFORE', '865 Research ParkwayBEFORE', 'Academic CenterBEFORE', 'Adams Center DormBEFORE', 'Adams HallBEFORE', 'Archeological Survey BuildingBEFORE', 'ArmoryBEFORE', 'Bizzell LibraryBEFORE', 'Buchanan HallBEFORE', 'Burton HallBEFORE', 'Carnegie BuildingBEFORE', 'Carpenter HallBEFORE', 'Carson Engr CtrBEFORE', 'Cate Center OneBEFORE', 'Cate Center TwoBEFORE', 'Cate Dorm #4BEFORE', 'Catlett Music CtrBEFORE', 'Ceramics StudioBEFORE', 'Chem Bldg AnnexBEFORE', 'Chemistry BuildingBEFORE', 'College of Allied HealthBEFORE', 'Collings HallBEFORE', 'Collums BuildingBEFORE', 'Comp Wind TunnelBEFORE', 'Copeland HallBEFORE', 'Cross Center ABEFORE', 'Dale HallBEFORE', 'Dale Hall TowerBEFORE', 'Devon Energy HallBEFORE', 'Dunham Residential CollegeBEFORE', 'Engineering LabBEFORE', 'Evans HallBEFORE', 'Farzaneh HallBEFORE', 'Fears Structural Engr LabBEFORE', 'Felgar HallBEFORE', 'Fine Arts CenterBEFORE', 'Five Partners PlaceBEFORE', 'Fred Jones Art CtrBEFORE', 'Fred Jones Art MuseumBEFORE', 'Fredrick Douglass CenterBEFORE', 'G L Cross HallBEFORE', 'Gaylord HallBEFORE', 'Gould HallBEFORE', 'HSC Conference CenterBEFORE', 'Headington HallBEFORE', 'Headington Residential CollegeBEFORE', 'Honors #5BEFORE', 'Huston Huffman CenterBEFORE', 'Intramural Soccer FieldBEFORE', 'Kaufman HallBEFORE', 'Law CenterBEFORE', 'Lawton Eisenhower High SchoolBEFORE', 'Lawton MacArthur High SchoolBEFORE', 'Lissa and Cy Wagner HallBEFORE', 'Lloyd Noble CenterBEFORE', 'Main Building - TexomaBEFORE', 'Michael F. Price HallBEFORE', 'Model ShopBEFORE', 'Monnet HallBEFORE', 'Moore Public SchoolsBEFORE', 'N.C. Bldg 101BEFORE', 'N.C. Bldg 104BEFORE', 'N.C. Bldg 210BEFORE', 'National Weather CenterBEFORE', 'Nielsen HallBEFORE', 'Noble MicroscopyBEFORE', 'Norman High SchoolBEFORE', 'Norman North High SchoolBEFORE', 'North Campus Aviation ComplexBEFORE', 'OU HSC Bird LibraryBEFORE', 'Oklahoma City Design CenterBEFORE', 'Oklahoma Memorial StadiumBEFORE', 'Oklahoma Memorial UnionBEFORE', 'Old Faculty ClubBEFORE', 'ParkwaysBEFORE', 'Physical Science CtrBEFORE', 'Putnam City School Admin OffBEFORE', 'Radar Innovations LabBEFORE', 'Rawls Engr Practice FacilityBEFORE', 'Reynolds Performing Arts CtrBEFORE', 'Richards HallBEFORE', 'Richards Hall AddBEFORE', 'Robertson HallBEFORE', 'S.C. Building 134BEFORE', 'SJ Sarkeys ComplexBEFORE', 'Sam Noble OK Museum Nat HistBEFORE', 'Sarkeys Energy CtrBEFORE', 'Science HallBEFORE', 'Southmoore Hish SchoolBEFORE', 'Stephenson Life Sci ResearchBEFORE', 'Stephenson Res and Tech. CntrBEFORE', 'Sutton HallBEFORE', 'Three Partners PlaceBEFORE', 'Zarrow HallBEFORE']
    enroll_now = ['655 Research ParkwayNOW', '825 Research ParkwayNOW', '865 Research ParkwayNOW', 'Academic CenterNOW', 'Adams Center DormNOW', 'Adams HallNOW', 'Archeological Survey BuildingNOW', 'ArmoryNOW', 'Bizzell LibraryNOW', 'Buchanan HallNOW', 'Burton HallNOW', 'Carnegie BuildingNOW', 'Carpenter HallNOW', 'Carson Engr CtrNOW', 'Cate Center OneNOW', 'Cate Center TwoNOW', 'Cate Dorm #4NOW', 'Catlett Music CtrNOW', 'Ceramics StudioNOW', 'Chem Bldg AnnexNOW', 'Chemistry BuildingNOW', 'College of Allied HealthNOW', 'Collings HallNOW', 'Collums BuildingNOW', 'Comp Wind TunnelNOW', 'Copeland HallNOW', 'Cross Center ANOW', 'Dale HallNOW', 'Dale Hall TowerNOW', 'Devon Energy HallNOW', 'Dunham Residential CollegeNOW', 'Engineering LabNOW', 'Evans HallNOW', 'Farzaneh HallNOW', 'Fears Structural Engr LabNOW', 'Felgar HallNOW', 'Fine Arts CenterNOW', 'Five Partners PlaceNOW', 'Fred Jones Art CtrNOW', 'Fred Jones Art MuseumNOW', 'Fredrick Douglass CenterNOW', 'G L Cross HallNOW', 'Gaylord HallNOW', 'Gould HallNOW', 'HSC Conference CenterNOW', 'Headington HallNOW', 'Headington Residential CollegeNOW', 'Honors #5NOW', 'Huston Huffman CenterNOW', 'Intramural Soccer FieldNOW', 'Kaufman HallNOW', 'Law CenterNOW', 'Lawton Eisenhower High SchoolNOW', 'Lawton MacArthur High SchoolNOW', 'Lissa and Cy Wagner HallNOW', 'Lloyd Noble CenterNOW', 'Main Building - TexomaNOW', 'Michael F. Price HallNOW', 'Model ShopNOW', 'Monnet HallNOW', 'Moore Public SchoolsNOW', 'N.C. Bldg 101NOW', 'N.C. Bldg 104NOW', 'N.C. Bldg 210NOW', 'National Weather CenterNOW', 'Nielsen HallNOW', 'Noble MicroscopyNOW', 'Norman High SchoolNOW', 'Norman North High SchoolNOW', 'North Campus Aviation ComplexNOW', 'OU HSC Bird LibraryNOW', 'Oklahoma City Design CenterNOW', 'Oklahoma Memorial StadiumNOW', 'Oklahoma Memorial UnionNOW', 'Old Faculty ClubNOW', 'ParkwaysNOW', 'Physical Science CtrNOW', 'Putnam City School Admin OffNOW', 'Radar Innovations LabNOW', 'Rawls Engr Practice FacilityNOW', 'Reynolds Performing Arts CtrNOW', 'Richards HallNOW', 'Richards Hall AddNOW', 'Robertson HallNOW', 'S.C. Building 134NOW', 'SJ Sarkeys ComplexNOW', 'Sam Noble OK Museum Nat HistNOW', 'Sarkeys Energy CtrNOW', 'Science HallNOW', 'Southmoore Hish SchoolNOW', 'Stephenson Life Sci ResearchNOW', 'Stephenson Res and Tech. CntrNOW', 'Sutton HallNOW', 'Three Partners PlaceNOW', 'Zarrow HallNOW', ]
    enroll_after = ['655 Research ParkwayAFTER', '825 Research ParkwayAFTER', '865 Research ParkwayAFTER', 'Academic CenterAFTER', 'Adams Center DormAFTER', 'Adams HallAFTER', 'Archeological Survey BuildingAFTER', 'ArmoryAFTER', 'Bizzell LibraryAFTER', 'Buchanan HallAFTER', 'Burton HallAFTER', 'Carnegie BuildingAFTER', 'Carpenter HallAFTER', 'Carson Engr CtrAFTER', 'Cate Center OneAFTER', 'Cate Center TwoAFTER', 'Cate Dorm #4AFTER', 'Catlett Music CtrAFTER', 'Ceramics StudioAFTER', 'Chem Bldg AnnexAFTER', 'Chemistry BuildingAFTER', 'College of Allied HealthAFTER', 'Collings HallAFTER', 'Collums BuildingAFTER', 'Comp Wind TunnelAFTER', 'Copeland HallAFTER', 'Cross Center AAFTER', 'Dale HallAFTER', 'Dale Hall TowerAFTER', 'Devon Energy HallAFTER', 'Dunham Residential CollegeAFTER', 'Engineering LabAFTER', 'Evans HallAFTER', 'Farzaneh HallAFTER', 'Fears Structural Engr LabAFTER', 'Felgar HallAFTER', 'Fine Arts CenterAFTER', 'Five Partners PlaceAFTER', 'Fred Jones Art CtrAFTER', 'Fred Jones Art MuseumAFTER', 'Fredrick Douglass CenterAFTER', 'G L Cross HallAFTER', 'Gaylord HallAFTER', 'Gould HallAFTER', 'HSC Conference CenterAFTER', 'Headington HallAFTER', 'Headington Residential CollegeAFTER', 'Honors #5AFTER', 'Huston Huffman CenterAFTER', 'Intramural Soccer FieldAFTER', 'Kaufman HallAFTER', 'Law CenterAFTER', 'Lawton Eisenhower High SchoolAFTER', 'Lawton MacArthur High SchoolAFTER', 'Lissa and Cy Wagner HallAFTER', 'Lloyd Noble CenterAFTER', 'Main Building - TexomaAFTER', 'Michael F. Price HallAFTER', 'Model ShopAFTER', 'Monnet HallAFTER', 'Moore Public SchoolsAFTER', 'N.C. Bldg 101AFTER', 'N.C. Bldg 104AFTER', 'N.C. Bldg 210AFTER', 'National Weather CenterAFTER', 'Nielsen HallAFTER', 'Noble MicroscopyAFTER', 'Norman High SchoolAFTER', 'Norman North High SchoolAFTER', 'North Campus Aviation ComplexAFTER', 'OU HSC Bird LibraryAFTER', 'Oklahoma City Design CenterAFTER', 'Oklahoma Memorial StadiumAFTER', 'Oklahoma Memorial UnionAFTER', 'Old Faculty ClubAFTER', 'ParkwaysAFTER', 'Physical Science CtrAFTER', 'Putnam City School Admin OffAFTER', 'Radar Innovations LabAFTER', 'Rawls Engr Practice FacilityAFTER', 'Reynolds Performing Arts CtrAFTER', 'Richards HallAFTER', 'Richards Hall AddAFTER', 'Robertson HallAFTER', 'S.C. Building 134AFTER', 'SJ Sarkeys ComplexAFTER', 'Sam Noble OK Museum Nat HistAFTER', 'Sarkeys Energy CtrAFTER', 'Science HallAFTER', 'Southmoore Hish SchoolAFTER', 'Stephenson Life Sci ResearchAFTER', 'Stephenson Res and Tech. CntrAFTER', 'Sutton HallAFTER', 'Three Partners PlaceAFTER', 'Zarrow HallAFTER']

    columns = lot_info + date_info + enroll_before + enroll_now + enroll_after + ['occ']
    data = get_data(columns=columns)

    reg = RandomForestRegressor(n_estimators=50)

    lots = ['Boyd House', 'Duck Pond', 'Jenkins', 'Monett Lot - North']
    lot_data = []
    for lot in lots:
        df = data[data['lot'] == lot].drop(columns='lot')

        train, test = train_test_split(df)

        lot_data.append((lot, train, test))

    for lot_name, train, test in lot_data:
        X_cols, X_train, y_train = x_y(train)
        reg.fit(X_train,y_train)

        print(lot_name) # Lot name
        if hasattr(reg, 'feature_importances_'):
            best_features = sorted(enumerate(reg.feature_importances_), key=lambda x: -x[1])[:10]
        if hasattr(reg, 'coef_'):
            best_features = sorted(enumerate(reg.coef_), key=lambda x: -x[1])[:10]
        print([(X_cols[i], score) for (i, score) in best_features])

        _, X_test, y_test = x_y(test)
        predict_test = reg.predict(X_test)

        print(reg.score(X_test, y_test))
        print("RMSE:", sqrt(mean_squared_error(y_test, predict_test)))

        plt.title(lot_name)
        plt.plot(y_test, label="True")
        plt.plot(predict_test, label="Predict")
        plt.legend()
        plt.show()


if __name__ == '__main__':
    main()