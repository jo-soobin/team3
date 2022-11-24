from django.views import generic
from .models import Post, Photo
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from folium import plugins
import folium
import geocoder

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def create(request):
    if(request.method == 'POST'):
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.pub_date = timezone.datetime.now()
        post.user = request.user
        post.save()
        # name 속성이 imgs인 input 태그로부터 받은 파일들을 반복문을 통해 하나씩 가져온다
        for img in request.FILES.getlist('imgs'):
            # Photo 객체를 하나 생성한다.
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = post
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            # 데이터베이스에 저장
            photo.save()
        return redirect('/detail/' + str(post.id))
    else:
        return render(request, 'new.html')

g = geocoder.ip('me')   #현재 내위치
# Create your views here.
def map(request) :
    map = folium.Map(location=g.latlng,zoom_start=15, width='100%', height='100%',)
    plugins.LocateControl().add_to(map)

    maps=map._repr_html_()  #지도를 템플릿에 삽입하기위해 iframe이 있는 문자열로 반환 (folium)
    return render(request,'../templates/map.html',{'map' : maps})