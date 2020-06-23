
import pandas as pd
import optical_switch
import time as t

class sun2lab:

    def __init__(self, size=100):

        self.labStatus = "Not Initialised"
        print("Initialising Lab ...")
        print("Initialising Optical Switch")
        self.oswitch = optical_switch.OpticalSwitch(host="192.168.0.2")  # Update hostname!
      #  self.oswitch.get()

        t.sleep(1)
        self.labStatus = "Initialised"
        print("Laboratory successfully initialised.")


        self.device_name = ['TLS', 'ODF1', 'ODF2',
                            'PRE1', 'PRE2', 'BOO1', 'BOO2',
                            'VOA1', 'VOA2',
                            'SPL1', 'SPL2',
                            'WSS1', 'WSS2',
                            'PMR1', 'PMR2', 'OMA',
                           ]
        self.indx = pd.Series(self.device_name)

        self.df = pd.DataFrame(data={

           'USER': [None, None, None,
                    None, None, None, None,
                    None, None,
                    None, None,
                    None, None,
                    None, None, None,


                                                ],
           'PORT_INPUT': [None, None, None,                 # inputs
                          '19', '20', '21', '22',             #Amp                      '19', '20', '21', '22',
                           '17', '18',                        #Attenuator
                          '25', '26',                     #Splitter
                            '23', '24',                      #Wsv
                           '27', '28', '29',               #Ouput

                                                     ],
           'PORT_OUTPUT': ['1', '2', '3',
                            '6', '7', '8', '9',            #Amp
                            '4', '5',                        #Attenuator  '4', '5',
                            '12', '13',                        #Splitter
                           '10', '11',                          #Wsv
                            None, None, None,],

           'TYPE':['IN', 'IN', 'IN',
                    'AM', 'AM', 'AM', 'AM',
                    'ATT', 'ATT',
                    'SPL', 'SPL',
                    'WSP', 'WSP',
                    'OUT', 'OUT', 'OUT', ]},

                                  columns=['USER', 'PORT_INPUT',  'PORT_OUTPUT',  'TYPE'],

                                  index= self.indx

                               )

    def get_unreserved_input(self):

        return self.df


    def set_reserved_input(self, userx, inputx ):

        self.df.at[inputx, 'USER']= userx
        print(self.df)


    def set_reserved_devs(self, userx, devx):

        self.df.at[devx, 'USER'] = userx
        print(self.df)


    def set_reserved_out(self, userx, outx):

        self.df.at[outx, 'USER'] = userx
        print(self.df)


    def set_reserved_conn(self, userx, inputx, ampx, attx, splx, wsvx, outx):

        seqlist =[inputx, ampx, attx, splx, wsvx, outx]

        list2 = list(filter(str.strip, seqlist))

        for i in range(len(list2) - 1):


            print("Connect :", self.df.loc[list2[i], 'PORT_OUTPUT'], "to ",
                      self.df.loc[list2[i + 1], 'PORT_INPUT'])
            self.oswitch.add_cross_connections(self.df.loc[list2[i], 'PORT_OUTPUT'],
                                               self.df.loc[list2[i + 1], 'PORT_INPUT'])

