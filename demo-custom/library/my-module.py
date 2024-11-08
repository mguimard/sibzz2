
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            my_arg=dict(type='str', default='default value'),
            my_arg_2=dict(type='str', required=True)
        ),
        supports_check_mode=True
    )

    # code super évolué.....

    changed = False

    if(module.params['my_arg'] == 'hello'):
        changed=True

    result = dict(
        changed=changed,
        courses="bieres"
    )

    module.exit_json(**result)


if __name__ == '__main__':
    main()
