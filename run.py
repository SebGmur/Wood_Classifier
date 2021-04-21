# Here we are creating entry point to our application
# Entry point has to be in the root of application folder/package

from app import app



if __name__ == "__main__":
    app.run(debug=True)