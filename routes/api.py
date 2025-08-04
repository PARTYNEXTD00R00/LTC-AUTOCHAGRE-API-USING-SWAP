from flask import Blueprint ,render_template,request,session
from services.common_utils import isGetStatus,isGetAddress

bp = Blueprint("api",__name__,url_prefix="/api/v1")


@bp.route('/ltc/status',methods=["POST"])
def api_get_status():
    get_status = isGetStatus()
    return get_status

@bp.route('/ltc/get',methods=["POST"])
def api_get():
    get_address = isGetAddress()
    return get_address
