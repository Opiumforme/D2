import sentry_sdk
sentry_sdk.init(
    "https://bfc844c58c804666a4873c2dfe157ace@o1005073.ingest.sentry.io/5965960",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

division_by_zero = 1 / 0