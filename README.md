Django Fragment Cache
===============

Django provides template fragment caching, such as :
```
{% load cache %}
{% cache 500 sidebar %}
    .. sidebar ..
{% endcache %}
```
But the variable `sidebar` still to be passed to the template every time, otherwise the fragment is blank when the cache expires.

If the data acquisition process is time consuming, then the fragment cache is to exist in name only.

So, this module provides another way to use the template cache.

## How to use?

### Install
```
pip install django-fragment-cache
```
Install Requires:
- django >= 2

edit your settings.py to add `fragment_cache` to your `NSTALLED_APPS`.
```
INSTALLED_APPS = (
    ...
    'fragment_cache',
    ...
)
```

### Use
you need provide a callable object to tell module how to get data, and the function return a dict.

**only call function when cache expires.**

```
import time
def get_data(num=10):
    time.sleep(3)
    return {'nums': list(range(num))}

def test(request):
    return render(request, 'test.html', {'get_data': get_data})
```

The `{% fragment_cache %}` template tag is similar to `{% cache %}` , for example:
```
{% load fragment_cache %}
{% fragment_cache 500 get_data %}
    <ul>
        {% for i in nums %}
            <li> {{ i }}</li>
        {% endfor %}
    </ul>
{% endfragment_cache %}
```
Sometimes, you might want to cache multiple copies of a fragment depending on some dynamic data that appears inside the fragment.

This allows different parameters to be cached to cache different results, for example:
```
{% load fragment_cache %}
{% fragment_cache 500 get_data 6 %}
    <ul>
        {% for i in nums %}
            <li> {{ i }}</li>
        {% endfor %}
    </ul>
{% endfragment_cache %}
```

Enjoy yourself.