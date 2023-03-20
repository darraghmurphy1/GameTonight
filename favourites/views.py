from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from social.models import Post
from .models import Favourite
from .forms import FavouriteForm


@login_required
def show_favourite(request):
    """ A view to show the user's post favourites """
    user = request.user
    favourites = Favourite.objects.filter(user=user)

    template = 'favourite.html'

    context = {
        'favourites': favourites,
    }

    return render(request, template, context)


@login_required
def add_favourite(request, post_id):
    """ Display form to add a favourite to a post """
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    user_favourite = Favourite.objects.filter(
        user=user, post=post)

    # Check if user already submitted a favourite for the post
    if user_favourite:
        messages.error(request,
                       'You have already added this')
        return redirect(reverse('post_detail', args=[post.slug]))
    else:
        if request.method == 'POST':
            form = FavouriteForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.user = request.user
                form.instance.post = post
                form.save()
                messages.success(request,
                                 'Your post favourite has been submitted')

                return redirect(reverse('post_detail', args=[post.slug]))
            else:
                messages.error(request, 'Failed to submit the favourite. \
                    Please ensure the form is valid.')
        else:
            form = FavouriteForm()

    template = 'add_favourite.html'

    context = {
        'post': post,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_favourite(request, favourite_id):
    """ Delete an existing favourite """
    favourite = get_object_or_404(Favourite, pk=favourite_id)

    if request.user != favourite.user:
        messages.error(request, 'You are not authorized \
            to delete this favourite.')
        return redirect(reverse('post_detail', args=[favourite.post.slug]))

    favourite.delete()
    messages.success(request, 'Your favourite has been deleted!')
    print('favourite', favourite)

    return redirect(reverse('post_detail', args=[favourite.post.slug]))