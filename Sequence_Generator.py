import numpy as np
import pandas as pd
import openpyxl

class TopoPhaseTracker:
    def __init__(self, phases=["AB", "BA"], initial_phase=0):
        self._phase = initial_phase
        self._phases = phases
        self._max_phase = len(self._phases)

    @property
    def phase(self):
        return self._phase

    @property
    def phases(self):
        return self._phases

    def current(self):
        return self._phases[self._phase]

    def next(self):

        self._phase = (self._phase + 1) % self._max_phase

        return self._phases[self._phase]

# Calls the Seqgenerator class and allows for user input of variables, this class object is initialized with these values "Kimosabi"
class SequenceGenerator:
    # Dictionary of Topos mapped to corresponding binary , shared across all classes Technically a self variable
    topo_binary = dict(Topo1="00", Topo2="00", Topo3="01", Topo4="01", Topo5="10", Topo6="10", Topo7="11", Topo8="11")

    def __init__(self, rounds, num_sequences, topo_sequence_input,topo_sequence):
        self.rounds = rounds
        self.num_sequences = num_sequences
        self.topo_sequence_input = topo_sequence_input
        self.topo_sequence = topo_sequence

    def info(self):
        print(f'rounds,num_seq,Topoinput,toposeq: {rounds,num_sequences,topo_sequence_input,topo_sequence}')

    def convert(self):
        final_sequence = []
        non_sep_seq = []

#Uncomment to see what all the passed in variables are
        #self.info()

        for num in range(self.num_sequences):
            topo_lists = self.topo_sequence_input.split(',')
            topo_sequence.append(topo_lists)

        # Converts Topo Sequence into Binary form
        for index, topo in enumerate(self.topo_sequence):
            for index2, num in enumerate(topo):
                topo_sequence[index][index2] = self.topo_binary[num]

        for ind, sequence in enumerate(self.topo_sequence):
            final_tracker = TopoPhaseTracker(sequence)
            for round in range(self.rounds):
                test = final_tracker.current()
                # adds test as a list to topo_sequence
                self.topo_sequence = non_sep_seq.append(test)
                final_tracker.next()

        # counter allows for indexing over across the total sequence to the individual locations by multiples of the number of rounds
        counter = 0
        # seperates the full list of binary into the individual unique sequences
        for num in range(self.num_sequences):
            sequence_num = self.rounds + counter - 1
            # this will go through and pull the sequence starting at 0 and goes to the length of inputted rounds that will then cut at the number of rounds
            generated_sequence = non_sep_seq[counter:(sequence_num)]
            # concatinates into one long string
            generated_sequence = ''.join(generated_sequence)
            final_sequence.append(generated_sequence)
            counter += self.rounds


        # Exporting to Excel sheet
        excel_data = pd.DataFrame(final_sequence)
        # populates custom_sequence sheet in local python/projects directory
        excel_data.to_excel('./custom_sequence.xlsx', sheet_name='Test Case 1', header=False, index=False)
        print(excel_data)

# outside the above class function
if __name__ == "__main__":

    # Dictionary of Topos mapped to corresponding binary
    topo_binary = dict(Topo1="00", Topo2="00", Topo3="01", Topo4="01", Topo5="10", Topo6="10", Topo7="11", Topo8="11")
    #lists variables to be populated
    topo_sequence = []
    unique_sequence = []
    final_sequence = []
    non_sep_seq = []

#Gathers the number of rounds that will be run in the experiment
    print("Input Number of Rounds: ")
    rounds = int(input())
    print("Input Number of Unique Sequences: ")
    num_sequences = int(input())
    print("Example of Unique Sequence: Topo1,Topo2,Topo3,Topo4,Topo5,Topo6,Topo7,Topo8")
#Allows user to input all unique sequences that they want to use for experiment
    print("Input Unique Sequence To Be Repeated Separate By Comma : ")
    for num in range(num_sequences):
        print(f"Input Unique Sequence # {num+1} To Be Repeated Separate By Comma : ")
        topo_sequence_input = str(input())
        topo_list = topo_sequence_input.split(',')
        topo_sequence.append(topo_list)
    print(topo_sequence)
    #Calls the Seqgenerator class and allows for user input of variables, this class object is initialized with these values "Kimosabi"  object that you created
    seq = SequenceGenerator(rounds, num_sequences, topo_sequence_input, topo_sequence)
    seq.convert()
