from flask import Flask, jsonify, request
from flask.views import MethodView
from db_app import *

app = Flask(__name__)


def get_Ads(ads_id: int, session: Session):
    ads = session.get(Ads, ads_id)
    return ads


class Ads_View(MethodView):

    def get(self, ads_id: int):
        with Session() as session:
            ads = get_Ads(ads_id, session)
            return jsonify(
                {
                "id": ads.id, "heading": ads.heading, "description": ads.description, "create_time": ads.create_time,
                "user": ads.user
                }
            )

    def post(self):
        json_data = request.json
        with Session() as session:
            ads = Ads(**json_data)
            session.add(ads)
            session.commit()
            return {'id': ads.id}

    def delete(self, ads_id: int):
        with Session() as session:
            ads = get_Ads(ads_id, session)
            session.delete(ads)
            session.commit()
            return jsonify({"status": "delete"})


app.add_url_rule('/ads/<int:ads_id>/', view_func=Ads_View.as_view('ads'), methods=['GET', 'DELETE'])
app.add_url_rule('/ads/', view_func=Ads_View.as_view('ads_create'), methods=['POST'])


if __name__=='__main__':
    app.run()

