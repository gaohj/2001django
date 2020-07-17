from django.core.management.base import BaseCommand
from cms.models import Article
from django.contrib.auth import get_user_model
from django.contrib.auth.models import ContentType,Group,Permission
User = get_user_model()
class Command(BaseCommand):

    def handle(self, *args, **options):
            #1管理员组添加权限 操作文章 操作用户
            admin_content_types = [
                ContentType.objects.get_for_model(User),
                ContentType.objects.get_for_model(Article),
            ]

            admin_permissions = Permission.objects.filter(content_type__in=admin_content_types)
            admin_group = Group.objects.create(name='管理员组')
            admin_group.permissions.set(admin_permissions)
            admin_group.save()

            self.stdout.write(self.style.SUCCESS('管理员组创建完成'))