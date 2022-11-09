from rest_framework import permissions


class IsOwnerReadOnly(permissions.BasePermission):
    """自定义权限： 只允许对象的所有者能够编辑"""

    def has_object_permission(self, request, view, obj):
        """
        所有的request都有读权限 因此一律允许GET/HEAD/OPTIONS方法
        :param request:
        :param view:
        :param obj:表的实例化对象
        :return: bool
        """

        # if request.method in ("GET", "HEAD", "OPTIONS"):
        if request.method in permissions.SAFE_METHODS:
            return True
        #对象的所有者才有写权限
        return request.user == obj.teacher

        # if request.user == obj.teacher:
        #     return True
        # if request.user != obj.teacher:
        #     return False