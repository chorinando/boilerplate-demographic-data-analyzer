import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load dataset
    df = pd.read_csv("adult.data.csv")  # Pastikan nama file sesuai

    # 1️⃣ Berapa banyak orang dari setiap ras?
    race_count = df["race"].value_counts()

    # 2️⃣ Berapa rata-rata umur laki-laki?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3️⃣ Berapa persentase orang yang memiliki gelar Bachelor's?
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # 4️⃣ Persentase orang dengan pendidikan tinggi (Bachelors, Masters, Doctorate) yang berpenghasilan >50K?
    higher_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_education_rich = round((df[higher_education]["salary"] == ">50K").mean() * 100, 1)

    # 5️⃣ Persentase orang tanpa pendidikan tinggi yang berpenghasilan >50K?
    lower_education = ~higher_education
    lower_education_rich = round((df[lower_education]["salary"] == ">50K").mean() * 100, 1)

    # 6️⃣ Berapa jumlah jam kerja minimum dalam seminggu?
    min_work_hours = df["hours-per-week"].min()

    # 7️⃣ Persentase orang yang bekerja jam minimum dengan gaji >50K?
    min_workers = df["hours-per-week"] == min_work_hours
    rich_percentage = round((df[min_workers]["salary"] == ">50K").mean() * 100, 1)

    # 8️⃣ Negara dengan persentase tertinggi orang yang berpenghasilan >50K?
    rich_by_country = df[df["salary"] == ">50K"]["native-country"].value_counts() / df["native-country"].value_counts()
    highest_earning_country = rich_by_country.idxmax()
    highest_earning_country_percentage = round(rich_by_country.max() * 100, 1)

    # 9️⃣ Pekerjaan paling umum bagi orang dengan penghasilan >50K di India?
    india_high_income = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    top_IN_occupation = india_high_income["occupation"].value_counts().idxmax()

    # Cetak hasil jika `print_data=True`
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print("Min work hours per week:", min_work_hours)
        print(f"Percentage of min work hours earners making >50K: {rich_percentage}%")
        print("Country with highest percentage earning >50K:", highest_earning_country)
        print(f"Highest earning country percentage: {highest_earning_country_percentage}%")
        print("Top occupation in India for those earning >50K:", top_IN_occupation)

    # Return dictionary sesuai format yang diminta freeCodeCamp
    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }
