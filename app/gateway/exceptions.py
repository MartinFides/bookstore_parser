class GatewayError(Exception):
    """Generic gateway error"""


class ResponseError(GatewayError):
    """Generic response error"""


class ForbiddenError(GatewayError):
    """Forbidden access error"""
