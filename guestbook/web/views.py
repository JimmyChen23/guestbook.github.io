from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Message
from .forms import MessageForm
from django.contrib.auth.mixins import LoginRequiredMixin

# 留言列表
class MessageList(ListView):
    model = Message
    ordering = ['-id']      # 以 id 欄位值由大至小反向排序

# 留言檢視
class MessageDetail(DetailView):
    model = Message

# 新增留言
class MessageCreate(CreateView):
    form_class = MessageForm
    success_url = "/"   
    template_name = 'form.html'   


# 刪除留言
class MessageDelete(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = '/message/'                # 刪除成功返回留言列表
    template_name = 'confirm_delete.html'

