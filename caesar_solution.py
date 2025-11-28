from Pyro4 import expose

class Solver:
    def __init__(self, workers=None, input_file_name=None, output_file_name=None, shift=3):
        self.workers = workers
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.shift = shift

    def solve(self):
        print("Job Started")
        print("Workers %d" % len(self.workers))

        # read input as full string
        text = self.read_input()

        part_size = len(text) // len(self.workers)
        mapped = []

        # MAP
        for i in range(len(self.workers)):
            start = i * part_size
            end = (i + 1) * part_size if i != len(self.workers) - 1 else len(text)
            part = text[start:end]
            mapped.append(self.workers[i].mymap(part, self.shift))

        # REDUCE
        result = self.myreduce(mapped)

        # write output
        self.write_output(result)

    @staticmethod
    @expose
    def mymap(text_part, shift):
        encrypted = ""
        for ch in text_part:
            if ch.isalpha():
                base = 'A' if ch.isupper() else 'a'
                encrypted += chr((ord(ch) - ord(base) + shift) % 26 + ord(base))
            else:
                encrypted += ch
        return encrypted

    @staticmethod
    @expose
    def myreduce(mapped):
        result = ""
        for p in mapped:
            result += p.value
        return result

    def read_input(self):
        with open(self.input_file_name, 'r') as f:
            return f.read()

    def write_output(self, output):
        with open(self.output_file_name, 'w') as f:
            f.write(output)
