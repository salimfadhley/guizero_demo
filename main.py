import logging
from guizero import App, Text

log: logging.Logger = logging.getLogger()

def make_app()->App:
    app = App(title="Hello world")
    message = Text(app, text="Welcome to the Hello world app!")
    return app


def main():
    logging.basicConfig()
    logging.getLogger("").setLevel(logging.INFO)

    log.info("Starting the app!")
    app:App = make_app()
    app.display()

if __name__ == "__main__":
    main()