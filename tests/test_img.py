try:
    from importlib import resources
except ImportError:
    import importlib_resources as resources


def get_image_path(filename):
    with resources.files('chico_dico.images').joinpath(filename) as path:
        return str(path)


if __name__ == '__main__':
    res = get_image_path('profile.jpg')
    print(res)
