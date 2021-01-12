from . import auth


@auth.route('/test', methods=['GET', 'POST'])
def test():
    return "Auth Route"
