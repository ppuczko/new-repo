#!/usr/bin/env python
################################################################################
#                                                                              #
# Copyright (c) 2015 Cisco Systems                                             #
# All Rights Reserved.                                                         #
#                                                                              #
#    Licensed under the Apache License, Version 2.0 (the "License"); you may   #
#    not use this file except in compliance with the License. You may obtain   #
#    a copy of the License at                                                  #
#                                                                              #
#         http://www.apache.org/licenses/LICENSE-2.0                           #
#                                                                              #
#    Unless required by applicable law or agreed to in writing, software       #
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT #
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the  #
#    License for the specific language governing permissions and limitations   #
#    under the License.                                                        #
#                                                                              #
################################################################################
"""
Simple application that logs on to the Switch and displays 
supervisor information
"""
import sys
import nxtoolkit.nxtoolkit as NX


def main():
    """
    Main execution routine

    :return: None
    """
    # Take login credentials from the command line if provided
    # Otherwise, take them from your environment variables file ~/.profile
    description = '''Simple application that logs on to the Switch and 
                    supervisor information.'''
    creds = NX.Credentials('switch', description)
    args = creds.get()

    # Login to Switch
    session = NX.Session(args.url, args.login, args.password)
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to Switch')
        sys.exit(0)

    # Download all of the interfaces
    # and store the data as tuples in a list
    data = []
    sups = NX.Supervisorcard.get(session)
    for sup in sups:
        data.append((sup.slot,
                          sup.model,
			  sup.serial,
                          sup.oper_st,
                          sup.num_ports,
                          sup.firmware,
                          sup.bios,
                          sup.hardware_version,
                          sup.hardware_revision))

    # Display the data downloaded
    template = "{0:5} {1:12} {2:^11} {3:^10} {4:9} {5:8} {6:6} {7:6} {8:6}"
    print(template.format("SLOT", "MODEL", "SERIAL NUM", "OPER STATE",
                        "NUM PORTS", "FIRMWARE", "BIOS", "HW VER", "HW REV"))
    print(template.format("----", "------------", "-----------", "----------",
                          "---------", "--------", "----", "------", "-----"))
    for rec in data:
        print(template.format(*rec))

if __name__ == '__main__':
    main()
