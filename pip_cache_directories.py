from pip._internal.utils.appdirs import user_cache_dir  # since pip v.10

print(user_cache_dir('pip'))
print(user_cache_dir('wheel'))
