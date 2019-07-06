import pytest
import numpy as np


def verify_out(capfd, expected):
    out, _ = capfd.readouterr()
    print(out)
    assert expected == out


flat_log_contents = {
    'head': '3c9530ac0da1106c0acbe1201900c51548bbcdd9',
    'ancestors': {
        '0ff3f2ec156ab8e1026b5271630ccae4556cc260': [''],
        '3c9530ac0da1106c0acbe1201900c51548bbcdd9': ['fed88489ab6e59913aee935169b15fe68755d82c'],
        'fed88489ab6e59913aee935169b15fe68755d82c': ['0ff3f2ec156ab8e1026b5271630ccae4556cc260']},
    'specs': {
        '0ff3f2ec156ab8e1026b5271630ccae4556cc260': {
            'commit_message': 'first commit adding training images and labels',
            'commit_time': 1562203787.257128, 'commit_user': 'Foo User', 'commit_email': 'foo@bar.com'},
        '3c9530ac0da1106c0acbe1201900c51548bbcdd9': {
            'commit_message': 'added testing labels only',
            'commit_time': 1562203787.388417, 'commit_user': 'Foo User', 'commit_email': 'foo@bar.com'},
        'fed88489ab6e59913aee935169b15fe68755d82c': {
            'commit_message': 'added testing images only',
            'commit_time': 1562203787.372292, 'commit_user': 'Foo User', 'commit_email': 'foo@bar.com'}},
    'order': ['3c9530ac0da1106c0acbe1201900c51548bbcdd9',
              'fed88489ab6e59913aee935169b15fe68755d82c',
              '0ff3f2ec156ab8e1026b5271630ccae4556cc260']}

flat_hash_branch_map = {
    '3c9530ac0da1106c0acbe1201900c51548bbcdd9': ['add-test'],
    '0ff3f2ec156ab8e1026b5271630ccae4556cc260': ['untouched-live-demo-branch']}


def test_flat_merge_graph(capfd):
    from hangar.diagnostics import Graph

    g = Graph(use_color=False)
    g.show_nodes(
        dag=flat_log_contents['ancestors'],
        spec=flat_log_contents['specs'],
        branch=flat_hash_branch_map,
        start=flat_log_contents['head'],
        order=flat_log_contents['order'],
        show_time=False,
        show_user=False)

    expected = '* 3c9530ac0da1106c0acbe1201900c51548bbcdd9 (add-test) : added testing labels only\n'\
               '* fed88489ab6e59913aee935169b15fe68755d82c : added testing images only\n'\
               '* 0ff3f2ec156ab8e1026b5271630ccae4556cc260 (untouched-live-demo-branch) : first commit adding training images and labels\n'

    verify_out(capfd, expected)


three_way_log_contents = {
    'head': '074f81d6b9fa5fa856175d47c7cc95cc4a839965',
    'ancestors': {
        '074f81d6b9fa5fa856175d47c7cc95cc4a839965': ['e5ea58dd9c7ffacd45fb128ddc00aced08d13889', '3c9530ac0da1106c0acbe1201900c51548bbcdd9'],
        'e5ea58dd9c7ffacd45fb128ddc00aced08d13889': ['0ff3f2ec156ab8e1026b5271630ccae4556cc260'],
        '0ff3f2ec156ab8e1026b5271630ccae4556cc260': [''],
        '3c9530ac0da1106c0acbe1201900c51548bbcdd9': ['fed88489ab6e59913aee935169b15fe68755d82c'],
        'fed88489ab6e59913aee935169b15fe68755d82c': ['0ff3f2ec156ab8e1026b5271630ccae4556cc260']},
    'specs': {
        '074f81d6b9fa5fa856175d47c7cc95cc4a839965': {
            'commit_message': 'adding in the new testing datasets',
            'commit_time': 1562203830.775428, 'commit_user': 'Foo User', 'commit_email': 'foo@bar.com'},
        'e5ea58dd9c7ffacd45fb128ddc00aced08d13889': {
            'commit_message': 'commit adding validation images and labels',
            'commit_time': 1562203787.320624, 'commit_user': 'Foo User', 'commit_email': 'foo@bar.com'},
        '0ff3f2ec156ab8e1026b5271630ccae4556cc260': {
            'commit_message': 'first commit adding training images and labels',
            'commit_time': 1562203787.257128, 'commit_user': 'Foo User', 'commit_email': 'foo@bar.com'},
        '3c9530ac0da1106c0acbe1201900c51548bbcdd9': {
            'commit_message': 'added testing labels only',
            'commit_time': 1562203787.388417, 'commit_user': 'Foo User', 'commit_email': 'foo@bar.com'},
        'fed88489ab6e59913aee935169b15fe68755d82c': {
            'commit_message': 'added testing images only',
            'commit_time': 1562203787.372292, 'commit_user': 'Foo User', 'commit_email': 'foo@bar.com'}},
    'order': ['074f81d6b9fa5fa856175d47c7cc95cc4a839965',
              '3c9530ac0da1106c0acbe1201900c51548bbcdd9',
              'fed88489ab6e59913aee935169b15fe68755d82c',
              'e5ea58dd9c7ffacd45fb128ddc00aced08d13889',
              '0ff3f2ec156ab8e1026b5271630ccae4556cc260']}

three_way_hash_branch_map = {
    '3c9530ac0da1106c0acbe1201900c51548bbcdd9': ['add-test'],
    'e5ea58dd9c7ffacd45fb128ddc00aced08d13889': ['add-validation'],
    '074f81d6b9fa5fa856175d47c7cc95cc4a839965': ['master'],
    '0ff3f2ec156ab8e1026b5271630ccae4556cc260': ['untouched-live-demo-branch']}


def test_three_way_merge_graph(capfd):
    from hangar.diagnostics import Graph

    g = Graph(use_color=False)
    g.show_nodes(
        dag=three_way_log_contents['ancestors'],
        spec=three_way_log_contents['specs'],
        branch=three_way_hash_branch_map,
        start=three_way_log_contents['head'],
        order=three_way_log_contents['order'],
        show_time=False,
        show_user=False)

    real = '*   074f81d6b9fa5fa856175d47c7cc95cc4a839965 (master) : adding in the new testing datasets\n'\
           '|\\  \n'\
           '| * 3c9530ac0da1106c0acbe1201900c51548bbcdd9 (add-test) : added testing labels only\n'\
           '| * fed88489ab6e59913aee935169b15fe68755d82c : added testing images only\n'\
           '* | e5ea58dd9c7ffacd45fb128ddc00aced08d13889 (add-validation) : commit adding validation images and labels\n'\
           '|/  \n'\
           '* 0ff3f2ec156ab8e1026b5271630ccae4556cc260 (untouched-live-demo-branch) : first commit adding training images and labels\n'

    verify_out(capfd, real)


octopus_log_contents = {
    'head': '05ad17beab54ede8d7f9214c5c6ae44509c3da97',
    'ancestors': {
        '05ad17beab54ede8d7f9214c5c6ae44509c3da97': ['b9c7da873c06c730f52bad5808df5312c4cc0a38', '1b49223ae5e731da3750e4836d14565dbe504f18'],
        'b9c7da873c06c730f52bad5808df5312c4cc0a38': ['a74236e598b96dcde10b176921eb58bb4a9c64bf', 'c4d6875caeff83a29413ae163dbcfdc3c57ad373'],
        'a74236e598b96dcde10b176921eb58bb4a9c64bf': ['9152a4578f74b36838f8187e43c8644b1eba47b5'],
        '9152a4578f74b36838f8187e43c8644b1eba47b5': ['ef7b6e5bcaaebf62b9e02902ff60eb7862c3472d', '21f274d31abc09ede4ad6753f079297885b02a09'],
        'ef7b6e5bcaaebf62b9e02902ff60eb7862c3472d': ['e9ca97e336496b1fceb75869adf0294af5635922'],
        'e9ca97e336496b1fceb75869adf0294af5635922': ['489bceb38246f27cae2a0f47eba0e488d95618db'],
        '489bceb38246f27cae2a0f47eba0e488d95618db': ['17286961175c5cbbd4381fef07cc0a20920a5ce6'],
        '17286961175c5cbbd4381fef07cc0a20920a5ce6': ['63ac654df43bd149a1ca5f919e714bc57e69af99'],
        '63ac654df43bd149a1ca5f919e714bc57e69af99': [''],
        '1b49223ae5e731da3750e4836d14565dbe504f18': ['9152a4578f74b36838f8187e43c8644b1eba47b5'],
        'c4d6875caeff83a29413ae163dbcfdc3c57ad373': ['63ac654df43bd149a1ca5f919e714bc57e69af99'],
        '21f274d31abc09ede4ad6753f079297885b02a09': ['5c0ea20c6513f135f0131d9e10d86801ded29537'],
        '5c0ea20c6513f135f0131d9e10d86801ded29537': ['10e84be056afb2ace6b7ba044ce1e9c9811eae4f'],
        '10e84be056afb2ace6b7ba044ce1e9c9811eae4f': ['e9ca97e336496b1fceb75869adf0294af5635922']},
    'specs': {
        '05ad17beab54ede8d7f9214c5c6ae44509c3da97': {'commit_message': 'try number two',
            'commit_time': 1562363265.6635652, 'commit_user': 'test user', 'commit_email': 'test@email.com'},
        'b9c7da873c06c730f52bad5808df5312c4cc0a38': {'commit_message': 'merging the long running branch into master',
            'commit_time': 1562363265.652887, 'commit_user': 'test user', 'commit_email': 'test@email.com'},
        'a74236e598b96dcde10b176921eb58bb4a9c64bf': {'commit_message': 'another on master',
            'commit_time': 1562363265.6346502, 'commit_user': 'test user', 'commit_email': 'test@email.com'},
        '9152a4578f74b36838f8187e43c8644b1eba47b5': {'commit_message': 'this is the first merge',
            'commit_time': 1562363265.578071, 'commit_user': 'test user', 'commit_email': 'test@email.com'},
        'ef7b6e5bcaaebf62b9e02902ff60eb7862c3472d': {'commit_message': 'third commit on master',
            'commit_time': 1562363265.4683158, 'commit_user': 'test user', 'commit_email': 'test@email.com'},
        'e9ca97e336496b1fceb75869adf0294af5635922': {'commit_message': 'second commit on master with training labels',
            'commit_time': 1562363265.398268, 'commit_user': 'test user', 'commit_email': 'test@email.com'},
        '489bceb38246f27cae2a0f47eba0e488d95618db': {'commit_message': 'second',
            'commit_time': 1562363264.7388191, 'commit_user': 'test user', 'commit_email': 'test@email.com'},
        '17286961175c5cbbd4381fef07cc0a20920a5ce6': {'commit_message': 'hi',
            'commit_time': 1562363264.735318, 'commit_user': 'test user', 'commit_email': 'test@email.com'},
        '63ac654df43bd149a1ca5f919e714bc57e69af99': {'commit_message': 'initial commit on master with training images',
            'commit_time': 1562363264.731286, 'commit_user': 'test user', 'commit_email': 'test@email.com'},
        '1b49223ae5e731da3750e4836d14565dbe504f18': {'commit_message': 'another on try delete',
            'commit_time': 1562363265.642503, 'commit_user': 'test user', 'commit_email': 'test@email.com'},
        'c4d6875caeff83a29413ae163dbcfdc3c57ad373': {'commit_message': 'first commit on the large branch',
            'commit_time': 1562363265.374819, 'commit_user': 'test user', 'commit_email': 'test@email.com'},
        '21f274d31abc09ede4ad6753f079297885b02a09': {'commit_message': 'another commit on test banch after adding to new_set',
            'commit_time': 1562363265.56455, 'commit_user': 'test user', 'commit_email': 'test@email.com'},
        '5c0ea20c6513f135f0131d9e10d86801ded29537': {'commit_message': 'second commit on test branch with new dset',
            'commit_time': 1562363265.545484, 'commit_user': 'test user', 'commit_email': 'test@email.com'},
        '10e84be056afb2ace6b7ba044ce1e9c9811eae4f': {'commit_message': 'first commit on test branch',
            'commit_time': 1562363265.524131, 'commit_user': 'test user', 'commit_email': 'test@email.com'}},
    'order': [
        '05ad17beab54ede8d7f9214c5c6ae44509c3da97',
        'b9c7da873c06c730f52bad5808df5312c4cc0a38',
        '1b49223ae5e731da3750e4836d14565dbe504f18',
        'a74236e598b96dcde10b176921eb58bb4a9c64bf',
        '9152a4578f74b36838f8187e43c8644b1eba47b5',
        '21f274d31abc09ede4ad6753f079297885b02a09',
        '5c0ea20c6513f135f0131d9e10d86801ded29537',
        '10e84be056afb2ace6b7ba044ce1e9c9811eae4f',
        'ef7b6e5bcaaebf62b9e02902ff60eb7862c3472d',
        'e9ca97e336496b1fceb75869adf0294af5635922',
        'c4d6875caeff83a29413ae163dbcfdc3c57ad373',
        '489bceb38246f27cae2a0f47eba0e488d95618db',
        '17286961175c5cbbd4381fef07cc0a20920a5ce6',
        '63ac654df43bd149a1ca5f919e714bc57e69af99']
    }

octopus_hash_branch_map = {
    'c4d6875caeff83a29413ae163dbcfdc3c57ad373': ['large_branch'],
    '21f274d31abc09ede4ad6753f079297885b02a09': ['test_branch'],
    '05ad17beab54ede8d7f9214c5c6ae44509c3da97': ['master'],
    '1b49223ae5e731da3750e4836d14565dbe504f18': ['trydelete']}


def test_octopus_merge_graph(capfd):
    from hangar.diagnostics import Graph

    g = Graph(use_color=False)
    g.show_nodes(
        dag=octopus_log_contents['ancestors'],
        spec=octopus_log_contents['specs'],
        branch=octopus_hash_branch_map,
        start=octopus_log_contents['head'],
        order=octopus_log_contents['order'],
        show_time=False,
        show_user=False)

    real = '*   05ad17beab54ede8d7f9214c5c6ae44509c3da97 (master) : try number two\n'\
           '|\\  \n'\
           '* \\   b9c7da873c06c730f52bad5808df5312c4cc0a38 : merging the long running branch into master\n'\
           '|\\ \\  \n'\
           '| | * 1b49223ae5e731da3750e4836d14565dbe504f18 (trydelete) : another on try delete\n'\
           '* | | a74236e598b96dcde10b176921eb58bb4a9c64bf : another on master\n'\
           '| |/  \n'\
           '|/|   \n'\
           '* |   9152a4578f74b36838f8187e43c8644b1eba47b5 : this is the first merge\n'\
           '|\\ \\  \n'\
           '| * | 21f274d31abc09ede4ad6753f079297885b02a09 (test_branch) : another commit on test banch after adding to new_set\n'\
           '| * | 5c0ea20c6513f135f0131d9e10d86801ded29537 : second commit on test branch with new dset\n'\
           '| * | 10e84be056afb2ace6b7ba044ce1e9c9811eae4f : first commit on test branch\n'\
           '* | | ef7b6e5bcaaebf62b9e02902ff60eb7862c3472d : third commit on master\n'\
           '|/ /  \n'\
           '* | e9ca97e336496b1fceb75869adf0294af5635922 : second commit on master with training labels\n'\
           '| * c4d6875caeff83a29413ae163dbcfdc3c57ad373 (large_branch) : first commit on the large branch\n'\
           '* | 489bceb38246f27cae2a0f47eba0e488d95618db : second\n'\
           '* | 17286961175c5cbbd4381fef07cc0a20920a5ce6 : hi\n'\
           '|/  \n'\
           '* 63ac654df43bd149a1ca5f919e714bc57e69af99 : initial commit on master with training images\n'

    verify_out(capfd, real)