class valCheck():
    def __init__(self, meanVct, meanScaler, meanB, sigmaVct, sigmaScaler, sigmaB):
        '''
        Continuous Check gives us a building block for actions that give a continuos result (like how long a hit was), instead of just sucseed/fail
        mean of action = meanScaler * (meanVct dot player skill vector) + meanB
        '''
        self.meanVct = np.array(meanVct)
        self.meanScaler = meanScaler
        self.meanB = meanB
        self.sigmaVct = np.array(sigmaVct)
        self.sigmaScaler = sigmaScaler
        self.sigmaB = sigmaB

    def run(self, sklVct):
        mean = self.meanScaler * (self.meanVct.dot(np.array(sklVct))) + self.meanB
        sigma = self.sigmaScaler * (self.sigmaVct.dot(np.array(sklVct))) + self.sigmaB
        return random.gauss(mean, sigma)
        