from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service
from utils import auth_required, admine_required
genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admine_required
    def  post(self):
        data = request.json
        genre_service.create(data)
        return "", 201


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admine_required
    def put(self,gid):
        data = request.json
        if gid not in data:
            data['id'] = gid
        genre_service.update(gid)
        return "", 201

    @admine_required
    def delete(self, gid):
        genre_service.delete(gid)
        return "", 204
