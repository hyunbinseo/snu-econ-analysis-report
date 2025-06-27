import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from prophet import Prophet
from skforecast.metrics import crps_from_quantiles
from sklearn.metrics import mean_absolute_error

holidaysDefault = pd.DataFrame(
    {
        "holiday": "default",
        "ds": pd.to_datetime(
            [
                "2018-01-01",
                "2018-02-15",
                "2018-02-16",
                "2018-02-17",
                "2018-03-01",
                "2018-05-05",
                "2018-05-07",
                "2018-05-22",
                "2018-06-06",
                "2018-06-13",
                "2018-08-15",
                "2018-09-23",
                "2018-09-24",
                "2018-09-25",
                "2018-09-26",
                "2018-10-03",
                "2018-10-09",
                "2018-12-25",
                "2019-01-01",
                "2019-02-04",
                "2019-02-05",
                "2019-02-06",
                "2019-03-01",
                "2019-05-05",
                "2019-05-06",
                "2019-05-12",
                "2019-06-06",
                "2019-08-15",
                "2019-09-12",
                "2019-09-13",
                "2019-09-14",
                "2019-10-03",
                "2019-10-09",
                "2019-12-25",
                "2020-01-01",
                "2020-01-24",
                "2020-01-25",
                "2020-01-26",
                "2020-01-27",
                "2020-03-01",
                "2020-04-15",
                "2020-04-30",
                "2020-05-05",
                "2020-06-06",
                "2020-08-15",
                "2020-09-30",
                "2020-10-01",
                "2020-10-02",
                "2020-10-03",
                "2020-10-09",
                "2020-12-25",
                "2021-01-01",
                "2021-02-11",
                "2021-02-12",
                "2021-02-13",
                "2021-03-01",
                "2021-05-05",
                "2021-05-19",
                "2021-06-06",
                "2021-08-15",
                "2021-09-20",
                "2021-09-21",
                "2021-09-22",
                "2021-10-03",
                "2021-10-09",
                "2021-12-25",
                "2022-01-01",
                "2022-01-31",
                "2022-02-01",
                "2022-02-02",
                "2022-03-01",
                "2022-03-09",
                "2022-05-05",
                "2022-05-08",
                "2022-06-01",
                "2022-06-06",
                "2022-08-15",
                "2022-09-09",
                "2022-09-10",
                "2022-09-11",
                "2022-09-12",
                "2022-10-03",
                "2022-10-09",
                "2022-10-10",
                "2022-12-25",
                "2023-01-01",
                "2023-01-21",
                "2023-01-22",
                "2023-01-23",
                "2023-01-24",
                "2023-03-01",
                "2023-05-05",
                "2023-05-27",
                "2023-05-29",
                "2023-06-06",
                "2023-08-15",
                "2023-09-28",
                "2023-09-29",
                "2023-09-30",
                "2023-10-02",
                "2023-10-03",
                "2023-10-09",
                "2023-12-25",
                "2024-01-01",
                "2024-02-09",
                "2024-02-10",
                "2024-02-11",
                "2024-02-12",
                "2024-03-01",
                "2024-04-10",
                "2024-05-05",
                "2024-05-06",
                "2024-05-15",
                "2024-06-06",
                "2024-08-15",
                "2024-09-16",
                "2024-09-17",
                "2024-09-18",
                "2024-10-01",
                "2024-10-03",
                "2024-10-09",
                "2024-12-25",
            ]
        ),
        "lower_window": 0,
        "upper_window": 0,
    }
)

holidaysAdded = pd.DataFrame(
    {
        "holiday": "added",
        "ds": pd.to_datetime(
            [
                "2018-01-01",
                "2018-02-15",
                "2018-02-16",
                "2018-02-17",
                "2018-02-18",
                "2018-03-01",
                "2018-05-05",
                "2018-05-06",
                "2018-05-07",
                "2018-05-22",
                "2018-06-06",
                "2018-06-13",
                "2018-08-15",
                "2018-09-22",
                "2018-09-23",
                "2018-09-24",
                "2018-09-25",
                "2018-09-26",
                "2018-10-03",
                "2018-10-09",
                "2018-12-25",
                "2019-01-01",
                "2019-02-02",
                "2019-02-03",
                "2019-02-04",
                "2019-02-05",
                "2019-02-06",
                "2019-03-01",
                "2019-03-02",
                "2019-03-03",
                "2019-05-04",
                "2019-05-05",
                "2019-05-06",
                "2019-05-11",
                "2019-05-12",
                "2019-06-06",
                "2019-08-15",
                "2019-09-12",
                "2019-09-13",
                "2019-09-14",
                "2019-09-15",
                "2019-10-03",
                "2019-10-09",
                "2019-12-25",
                "2020-01-01",
                "2020-01-24",
                "2020-01-25",
                "2020-01-26",
                "2020-01-27",
                "2020-02-29",
                "2020-03-01",
                "2020-04-15",
                "2020-04-30",
                "2020-05-05",
                "2020-06-06",
                "2020-06-07",
                "2020-08-15",
                "2020-08-16",
                "2020-09-30",
                "2020-10-01",
                "2020-10-02",
                "2020-10-03",
                "2020-10-04",
                "2020-10-09",
                "2020-10-10",
                "2020-10-11",
                "2020-12-25",
                "2020-12-26",
                "2020-12-27",
                "2021-01-01",
                "2021-01-02",
                "2021-01-03",
                "2021-02-11",
                "2021-02-12",
                "2021-02-13",
                "2021-02-14",
                "2021-02-27",
                "2021-02-28",
                "2021-03-01",
                "2021-05-05",
                "2021-05-19",
                "2021-06-05",
                "2021-06-06",
                "2021-08-14",
                "2021-08-15",
                "2021-09-18",
                "2021-09-19",
                "2021-09-20",
                "2021-09-21",
                "2021-09-22",
                "2021-10-02",
                "2021-10-03",
                "2021-10-09",
                "2021-10-10",
                "2021-12-25",
                "2021-12-26",
                "2022-01-01",
                "2022-01-02",
                "2022-01-29",
                "2022-01-30",
                "2022-01-31",
                "2022-02-01",
                "2022-02-02",
                "2022-03-01",
                "2022-03-09",
                "2022-05-05",
                "2022-05-06",
                "2022-05-07",
                "2022-05-08",
                "2022-06-01",
                "2022-06-04",
                "2022-06-05",
                "2022-06-06",
                "2022-08-13",
                "2022-08-14",
                "2022-08-15",
                "2022-09-09",
                "2022-09-10",
                "2022-09-11",
                "2022-09-12",
                "2022-10-01",
                "2022-10-02",
                "2022-10-03",
                "2022-10-08",
                "2022-10-09",
                "2022-10-10",
                "2022-12-24",
                "2022-12-25",
                "2022-12-31",
                "2023-01-01",
                "2023-01-21",
                "2023-01-22",
                "2023-01-23",
                "2023-01-24",
                "2023-03-01",
                "2023-05-05",
                "2023-05-06",
                "2023-05-07",
                "2023-05-27",
                "2023-05-28",
                "2023-05-29",
                "2023-06-06",
                "2023-08-15",
                "2023-09-28",
                "2023-09-29",
                "2023-09-30",
                "2023-10-01",
                "2023-10-02",
                "2023-10-03",
                "2023-10-07",
                "2023-10-08",
                "2023-10-09",
                "2023-12-23",
                "2023-12-24",
                "2023-12-25",
                "2023-12-30",
                "2023-12-31",
                "2024-01-01",
                "2024-02-09",
                "2024-02-10",
                "2024-02-11",
                "2024-02-12",
                "2024-03-01",
                "2024-03-02",
                "2024-03-03",
                "2024-04-10",
                "2024-05-04",
                "2024-05-05",
                "2024-05-06",
                "2024-05-15",
                "2024-06-06",
                "2024-08-15",
                "2024-09-14",
                "2024-09-15",
                "2024-09-16",
                "2024-09-17",
                "2024-09-18",
                "2024-10-01",
                "2024-10-02",
                "2024-10-03",
                "2024-10-09",
                "2024-12-25",
            ]
        ),
        "lower_window": 0,
        "upper_window": 0,
    }
)

date_column = "date"
value_column = "rental"

df = pd.read_csv("data.csv")
df[date_column] = pd.to_datetime(df[date_column])
df = df.sort_values(date_column).reset_index(drop=True)
df[f"{value_column}_log"] = np.log(df[value_column])

df_prophet = df[[date_column, f"{value_column}_log"]].copy()
df_prophet.columns = ["ds", "y"]
train_size = int(len(df_prophet) * 6 / 7)

df_train = df_prophet[:train_size]
df_test = df_prophet[train_size:]

p_series_actual = df_test["y"].reset_index(drop=True)


def run_prophet_model(
    holidays_df, holidays_name, df_train, df_test, train_size, p_series_actual
):
    model = Prophet(holidays=holidays_df)
    model.fit(df_train)

    future_dataframe = model.make_future_dataframe(periods=len(df_test))
    forecast = model.predict(future_dataframe)
    forecast_test = forecast[train_size:].copy()

    series_pred = forecast_test["yhat"].reset_index(drop=True)

    mae = mean_absolute_error(p_series_actual, series_pred)
    mape = np.mean(np.abs((p_series_actual - series_pred) / p_series_actual)) * 100
    crps = np.mean(
        [
            crps_from_quantiles(
                y_true=float(p_series_actual.iloc[i]),
                pred_quantiles=np.array(
                    [
                        forecast_test["yhat_lower"].iloc[i],
                        forecast_test["yhat_upper"].iloc[i],
                    ]
                ),
                quantile_levels=np.array([0.1, 0.9]),
            )
            for i in range(len(p_series_actual))
        ]
    )

    print(f"\nProphet Results with {holidays_name} (Log Scale):")
    print(f"MAE: {mae:.4f}")
    print(f"MAPE: {mape:.2f}%")
    print(f"CRPS: {crps:.4f}")

    model.plot(forecast)
    plt.title(f"Prophet Model Forecast with {holidays_name} - Full Timeline")
    plt.show()

    return {
        "model": model,
        "forecast": forecast,
        "forecast_test": forecast_test,
        "series_pred": series_pred,
        "mae": mae,
        "mape": mape,
        "crps": crps,
        "holidays_name": holidays_name,
    }


print("=" * 60)
print("RUNNING PROPHET MODEL WITH DEFAULT HOLIDAYS")
print("=" * 60)
default_results = run_prophet_model(
    holidaysDefault, "Default Holidays", df_train, df_test, train_size, p_series_actual
)

print("\n" + "=" * 60)
print("RUNNING PROPHET MODEL WITH ADDED HOLIDAYS")
print("=" * 60)
added_results = run_prophet_model(
    holidaysAdded, "Added Holidays", df_train, df_test, train_size, p_series_actual
)

print("\n" + "=" * 60)
print("COMPARISON OF RESULTS")
print("=" * 60)
print(
    f"{'Metric':<10} {'Default Holidays':<20} {'Added Holidays':<20} {'Improvement':<15}"
)
print("-" * 80)

# Define metrics and their formatting
metrics = [
    ("MAE", "mae", ".4f"),
    ("MAPE", "mape", ".2f"),
    ("CRPS", "crps", ".4f"),
]

for metric_name, metric_key, format_spec in metrics:
    default_value = default_results[metric_key]
    added_value = added_results[metric_key]
    improvement = ((default_value - added_value) / default_value) * 100

    print(
        f"{metric_name:<10} {default_value:<20{format_spec}} {added_value:<20{format_spec}} {improvement:>+15.2f}%"
    )
