---
- name: CONFIGURE IPv6 ADDRESSING
  hosts: CSR1kv
  gather_facts: false
  connection: local

  tasks:
   - name: SET IPv6 ON LOOPBACK33
     ios_config:
       parents: "interface Loopback33"
       lines:
         - description IPv6 Loopback
         - ipv6 address 3001:ABCD:ABCD:1::1/128
         - ipv6 address FE80::1 link-local

   - name: Show Running config
     ios_command:
       commands:
         - show running-config
     register: output

   - name: SAVE OUTPUT ./ios_backups/
     copy:
       content: "{{ output.stdout[0] }}"
       dest: "./IPv6_output_{{ inventory_hostname }}.txt"
     delegate_to: localhost