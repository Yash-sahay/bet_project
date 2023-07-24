from django.http import Http404, HttpResponseForbidden, HttpResponse


def role_validations(*groups):
    def decorator(function):
        def wrapper(request, *args, **kwargs):

            if request.user.groups.filter(name__in=groups).exists():
                return function(request, *args, **kwargs)
            else:
                res = HttpResponse("You are not allowed")
                return HttpResponseForbidden(res)
        return wrapper

    return decorator
