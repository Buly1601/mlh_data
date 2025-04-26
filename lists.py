libraries = {
    "python": [
        "numpy", "pandas", "matplotlib", "seaborn", "scikit-learn", "tensorflow", "pytorch", "xgboost", "lightgbm",
        "statsmodels", "plotly", "altair", "bokeh", "flask", "django", "fastapi", "requests", "httpx",
        "beautifulsoup4", "scrapy", "openpyxl", "xlrd", "pypdf2", "schedule", "click", "typer", "rich", "loguru",
        "pydantic", "pathlib", " os ", " sys ", "pytest", "unittest", "pillow", "opencv-python", "sqlalchemy", "alembic",
        "asyncio", "aiohttp", "pyyaml", "json", "dataclasses", "marshmallow", "joblib", "fabric", "gunicorn",
        "uvicorn", "celery", "redis", "pyarrow", "pyqt5", "pygame", "pyinstaller", "virtualenv", "pipenv", "black",
        "isort", "mypy", "jupyter", "notebook", "streamlit", "gradio", "transformers", "langchain", "spacy",
        "nltk", "gensim", "mlflow", "optuna", "boto3", "pytest-django", "pytest-cov", "httpie", "twilio", "paramiko",
        "flit", "sanic", "hug", "dash", "panel", "traitlets", "ipywidgets", "tqdm", "numba", "cupy",
        "pyomo", "sympy", "networkx", "graph-tool", "pyspark", "fuzzywuzzy", "textblob", "whoosh", "chardet",
        "watchdog", "email-validator", "pyright", "pyre-check"
    ],

    "c++": [
        "boost", "eigen", "opencv", "fmt", "spdlog", "protobuf", "grpc", "nlohmann-json", "poco", "cereal",
        "tbb", "catch2", "googletest", "rapidjson", "jsoncpp", "asio", "libcurl", "sqlite3", "curlpp", "qt",
        "wxwidgets", "sdl2", "glfw", "glew", "glm", "openal", "bullet", "irrlicht", "ogre3d", "cgal", "nanoflann",
        "xtensor", "armadillo", "ceres-solver", "dlib", "tinyxml2", "zlib", "libpng", "libjpeg", "ffmpeg",
        "portaudio", "yaml-cpp", "glog", "benchmark", "libtorch", "tesseract", "opencv-contrib", "libgit2",
        "libxml2", "clipp", "range-v3", "sol2", "entt", "box2d", "freetype", "xgboost", "mlpack", "opencl",
        "cuda", "thrust", "rocm", "vulkan-hpp", "vulkan-sdk", "directxmath", "llvm", "clang", "emscripten",
        "catch", "doctest", "qtcreator", "cmake", "make", "bazel", "ninja", "conan", "vcpkg", "gtest",
        "libevent", "libuv", "mariadb-connector-c", "mysql-connector-cpp", "sqlite-modern-cpp", "libcoap",
        "libmosquitto", "zeromq", "grpcpp", "protobuf-c", "flatbuffers", "capnproto", "rapidxml", "gflags",
        "re2", "abseil", "simdjson", "folly", "openmp", "mkl", "lapacke", "blas", "gdal", "geos", "proj"
    ],

    "c#": [
        "newtonsoft.json", "dapper", "serilog", "nlog", "log4net", "autofac", "unity.container", "structuremap",
        "xunit", "nunit", "moq", "restsharp", "fluentvalidation", "mediatr", "automapper", "polly", "hangfire",
        "identityserver", "mass-transit", "refit", "blazor", "entityframework", "efcore", "ml.net", "aspnetcore",
        "signalr", "swashbuckle", "bogus", "mapster", "flurl", "htmlagilitypack", "sqlite-net-pcl", "csla",
        "sharpziplib", "skia-sharp", "imagemagick.net", "microsoft.extensions.*", "bunit", "benchmarkdotnet",
        "chocolatey", "cake", "dotnet-script", "reactiveui", "avaloniaui", "mahapps.metro", "oxyplot",
        "livecharts", "serilog.sinks.*", "coverlet", "stylecop", "roslyn", "system.text.json", "grpc.net",
        "protobuf-net", "fastreport", "stimulsoft", "selenium", "specflow", "playwright", "cscore", "sharpdx",
        "openxml", "microsoft.graph", "azure.storage.blobs", "azure.identity", "awssdk", "json.net", "protobuf-net",
        "dotenv.net", "humanizer", "smartformat", "servicefabric", "webgrease", "libphonenumber-csharp",
        "sharpcompress", "zxing.net", "itext7", "dotnetzip", "minio", "mediakit", "microsoft.bot.builder",
        "graphql-dotnet", "easyhttp", "microsoft.aspnetcore.mvc", "identitymodel", "efcore.sqlserver",
        "efcore.sqlite", "squirrel.windows", "microsoft.extensions.configuration", "microsoft.extensions.logging",
        "microsoft.extensions.dependencyinjection", "microsoft.extensions.hosting", "dotnet-monitor", "healthchecks"
    ],

    "rust": [
        "serde", "tokio", "reqwest", "actix-web", "warp", "rocket", "hyper", "axum", "clap", "structopt",
        "anyhow", "thiserror", " log ", "env_logger", "tracing", "chrono", "regex", "sqlx", "diesel", "rusqlite",
        "sled", "mongodb", "postgres", "redis", "openssl", "rustls", "jsonwebtoken", "bcrypt", "argon2",
        "uuid", "lazy_static", "futures", "async-trait", "rayon", "crossbeam", "parking_lot", "dashmap",
        " tui ", "iced", "egui", "gtk-rs", "glium", "wgpu", "bevy", "amethyst", "ggez", "macroquad",
        "nannou", "kiss3d", "piston", "nalgebra", "cgmath", "hecs", "specs", "fltk-rs", "iced", "minifb",
        "crossterm", "termion", "rusttype", "unicode-segmentation", "num", "num-traits", "itertools",
        "bitflags", "prost", "tonic", "flatbuffers", "capnp", "bindgen", "cc", "criterion", "proptest",
        "quickcheck", "docopt", "getopts", "glob", "walkdir", "notify", "fs_extra", "tempfile", "tar",
        "zip", "flate2", "zstd", "bincode", "rmp-serde", " ron ", "csv", "petgraph", "plotters", "wasmtime",
        "wasmer", "rhai", "mlua", "dioxus", "leptos", "yew"
    ],

    "javascript": [
        "react", "vue", "angular", "svelte", "jquery", "lodash", "axios", "express", "next", "nuxt",
        "vite", "webpack", "babel", "eslint", "prettier", "rollup", "jest", "mocha", "chai", "vitest",
        "cypress", "puppeteer", "playwright", "ts-node", "typescript", "moment", "dayjs", "date-fns",
        "chart.js", "d3", "three", "gsap", "animejs", "leaflet", "socket.io", "redux", "mobx", "zustand",
        "react-query", "apollo-client", "graphql", "urql", "mongoose", "sequelize", "knex", "mysql2",
        "pg", "sqlite3", "passport", "jsonwebtoken", "bcryptjs", "argon2", "dotenv", "cors", "helmet",
        "multer", "nodemailer", "sharp", "uuid", "validator", "class-validator", "rxjs", "immer",
        "chalk", " ora ", "yargs", "commander", "inquirer", "husky", "lint-staged", "stylelint", "tailwindcss",
        "bootstrap", "material-ui", "chakra-ui", "ant-design", "emotion", "styled-components",
        "formik", "react-hook-form", "yup", "zod", "pixi.js", "phaser", "vitepress", "nuxt-content",
        "gridsome", "gatsby", "11ty", "next-auth", "firebase", "supabase", "strapi", "sanity", "keystone"
    ],

    "java": [
        "spring-boot", "spring-framework", "hibernate", "jakarta-ee", "micronaut", "quarkus", "dropwizard",
        "junit", "testng", "mockito", "log4j", "slf4j", "logback", "lombok", "mapstruct", "jackson",
        "gson", "retrofit", "okhttp", "spring-data", "mybatis", "jooq", "jpa", "flyway", "liquibase",
        "guava", "apache-commons", "rxjava", "vertx", "spark-java", "vaadin", "javafx", "swt",
        "thymeleaf", "freemarker", "mustache", "handlebars", "jsp", "servlet-api", "tomcat",
        "jetty", "undertow", "netty", "grpc-java", "protobuf-java", "kafka-clients", "activemq",
        "rabbitmq-java", "mongodb-driver", "neo4j-java-driver", "influxdb-java", "elasticsearch-rest-client",
        "hazelcast", "ehcache", "caffeine", "lettuce", "jedis", "redisson", "spring-security",
        "keycloak", "apache-shiro", "jwt", "jjwt", "bcprov", "bouncycastle", "httpclient", "commons-io",
        "commons-lang3", "commons-collections", "commons-math3", "joda-time", "opencsv", "poi", "itext",
        "pdfbox", "apache-tika", "java-mail", "jsoup", "slf4j-api", "micrometer", "prometheus-java",
        "newrelic", "datadog-api-client", "logstash-logback-encoder", "zookeeper", "curator", "spark",
        "hadoop", "hbase", "avro", "parquet", "snowflake-jdbc", "clickhouse-jdbc", "jgit", "jna",
        "junit5", "mockk", "hamcrest", "rest-assured", "awaitility"
    ]
}

langs = [
" c ",
"python",
"c++",
" java ",
"c#",
"javascript",
"sql",
"golang",
"typescript",
"php",
"kotlin",
"rust",
"react"]

frameworks = {
    "python": [
        "django", "flask", "fastapi", "pyramid", "tornado", "bottle", "hug", "falcon", "web2py", "sanic",
        "dash", "streamlit", "gradio", "panel", "pywebio", "plotly-dash", "scrapy", "spacy", "transformers", "mlflow"
    ],

    "c++": [
        "qt", "boost", "poco", "wxwidgets", "cinder", "juce", "openframeworks", "ogre3d", "irrlicht",
        "glfw", "sdl2", "cef", "folly", "caf", "drogon", "crow", "restbed", "ultralight", "wt", "chaiscript"
    ],

    "c#": [
        "aspnetcore", "blazor", "wpf", "winforms", " unity ", "xamarin", "avalonia", "mono", "uno-platform", "maui",
        "dotvvm", "orchardcore", "nopcommerce", "umbraco", "sitefinity", "kentico", "serenity", "abp", "servicefabric", "nancy"
    ],

    "rust": [
        "actix-web", "rocket", "warp", "axum", "tide", "gotham", "tower-web", "poem", "salvo", "dioxus",
        "leptos", "yew", "egui", "bevy", "amethyst", "macroquad", "ggez", "nannou", "fltk-rs", "iced"
    ],

    "javascript": [
        "react", "vue", "angular", "svelte", "nuxt", "express", "nest", "gatsby", "11ty",
        "meteor", "ember", "preact", "remix", "sapper", "koa", "fastify", "strapi", "keystone", "loopback"
    ],

    "java": [
        "spring-boot", "spring-framework", "micronaut", "quarkus", "dropwizard", "jakarta-ee", "jsf", "struts",
        "vaadin", "spark", "vertx", "grails", "play", "gwt", "blade", "javalin", "jooby", "ratpack", "hibernate", "mybatis"
    ]
}

features = [
    "user authentication", "real-time chat", "live notifications", "dark mode", "mobile responsiveness",
    "offline mode", "voice commands", "ai-generated content", "ml-based recommendations",
    "data visualization dashboards", "qr code scanner", "ocr (text from image)", "speech-to-text",
    "text-to-speech", "interactive maps", "geolocation tracking", "push notifications",
    "augmented reality view", "camera integration", "file upload/download", "live video streaming",
    "customizable user profiles", "admin dashboard", "gamification elements", "leaderboard",
    "collaborative editing", "markdown support", "api integration", "blockchain wallet",
    "crypto payments", "nfc/rfid support", "iot device control", "sensor data logging",
    "calendar/scheduling", "smart reminders", "image recognition", "sentiment analysis",
    "email/sms integration", "social media sharing", "web scraping", "browser extension",
    "command line interface", "drag-and-drop UI", "real-time collaboration", "multi-language support",
    "accessibility tools (a11y)", "custom themes", "data export (csv/json)", "role-based permissions",
    "automated testing", "ci/cd pipeline", "data encryption", "two-factor authentication", "biometric authentication",
    "cloud storage integration", "custom notifications", "data analytics", "video conferencing",
    "file versioning", "social login integration", "task automation", "personalized dashboards",
    "realtime data streaming", "weather data integration", "payment gateway integration", "customizable themes",
    "multi-user chat rooms", "image editing tools", "video editing tools", "drag-and-drop file management",
    "multi-platform sync", "AI chatbot", "customer support ticket system", "live polling",
    "real-time stock market data", "shopping cart", "search functionality", "product recommendations",
    "AI-driven content curation", "real-time voting system", "augmented reality filters", "object detection",
    "facial recognition", "content moderation", "fitness tracking", "automated data cleaning", "voice recognition",
    "smart home automation", "document scanning", "time tracking", "financial tracking", "voice-controlled UI",
    "health data integration", "energy consumption monitoring", "fitness challenges", "data visualization charts",
    "document sharing", "pdf generation", "version control system", "team collaboration features",
    "serverless architecture", "cloud deployment", "app deployment pipelines", "server monitoring",
    "AI-based text summarization", "real-time analytics", "API testing tools", "social sharing buttons",
    "peer-to-peer file sharing", "multi-device sync", "data backup", "job scheduling", "cloud functions",
    "AI-powered search", "language translation", "app cloning", "remote desktop control", "chatbot customer service",
    "QR code generation", "image search", "video summarization", "content scheduling", "price comparison tool"
]
