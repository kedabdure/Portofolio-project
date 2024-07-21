# Register blueprint api/v1 when the app call it by passing flask app to register
def create_api(app):
    from .v1 import api_v1
    app.register_blueprint(api_v1)
