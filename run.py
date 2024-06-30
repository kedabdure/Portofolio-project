from app import create_app

# call create_app function and assign Flask instance to app
app = create_app()

# run the flask app
if __name__ == '__main__':
    app.run(debug=True)
