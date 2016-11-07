import itertools

from django import forms
from django.contrib.auth.models import User
from django.utils.text import slugify
from sketchfab.models import Model3d

__author__ = 'Pierre Rodier | pierre@buffactory.com'


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class Model3dForm(forms.ModelForm):

    class Meta:
        model = Model3d
        fields = ['name', 'description', 'picture']

    def save(self, commit=True):
        """
        Custom saving method for Model3dForm.
        That method will generate a slug for the new Model3d and will ensure that this slug is unique.

        :param  commit:     If commit=True, then the changes to ``instance`` will be saved to the database
        :type   commit:     bool

        :return:    The created Model3d instance

        @see: original code from: https://keyerror.com/blog/automatically-generating-unique-slugs-in-django
        """
        instance = super(Model3dForm, self).save(commit=False)

        max_length = Model3d._meta.get_field('slug').max_length
        instance.slug = orig = slugify(instance.name)[:max_length]

        for x in itertools.count(1):
            if not Model3d.objects.filter(slug=instance.slug).exists():
                break
            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        if commit:
            instance.save()

        return instance
