
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            my_arg=dict(type='str', default='default value'),
        ),
        supports_check_mode=True
    )

    changed = False

    if(module.params['my_arg'] == "hello"):
        changed = True
        

    result = dict(
        changed=changed,
        some_key="hello world"
    )

    module.exit_json(**result)


if __name__ == '__main__':
    main()
