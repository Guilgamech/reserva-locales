from apps.user.models import User
from apps.local.models import Local


def sync_user_relations(user, ldap_attributes, *, connection=None, dn=None):
    print(user.email)
    local = Local.objects.filter(responsable_email=user.email).first()
    print(local)
    if local is not None:
        obj_user = User.objects.get(pk=user.pk)
        if obj_user is not None:
            obj_user.rol = 'Responsable'
            obj_user.save()

    print(ldap_attributes)
