# imports
from os import mkdir
import math
from statistics import median, stdev
from matplotlib import pyplot as plt
from time import gmtime, strftime, time
from random import uniform, choice, randint
import uuid


class DE:

    def __init__(self):
        self.pop = []  # population's positions
        self.m_nmdf = 0.00  # diversity variable
        self.diversity = []
        self.fbest_list = []

    def generateGraphs(self, fbest_list, diversity_list, max_iterations, uid, run):
        plt.plot(range(0, max_iterations), fbest_list, 'r--')
        plt.savefig(str(uid) + '/graphs/run' + str(run) + '_' + 'convergence.png')
        plt.clf()
        plt.plot(range(0, max_iterations), diversity_list, 'b--')
        plt.savefig(str(uid) + '/graphs/run' + str(run) + '_' + 'diversity.png')
        plt.clf()

    def updateDiversity(self):
        diversity = 0
        aux_1 = 0
        aux2 = 0
        a = 0
        b = 0
        d = 0

        for a in range(0, len(self.pop)):
            b = a + 1
            for i in range(b, len(self.pop)):
                aux_1 = 0

                ind_a = self.pop[a]
                ind_b = self.pop[b]

                for d in range(0, len(self.pop[0])):
                    aux_1 = aux_1 + (pow(ind_a[d] - ind_b[d], 2).real)
                aux_1 = (math.sqrt(aux_1).real)
                aux_1 = (aux_1 / len(self.pop[0]))

                if b == i or aux_2 > aux_1:
                    aux_2 = aux_1
            diversity = (diversity) + (math.log((1.0) + aux_2).real)

        if self.m_nmdf < diversity:
            self.m_nmdf = diversity

        return (diversity / self.m_nmdf).real

    # fitness_function
    def fitness(self, individual):
        'to override'
        'rastrigin'
        result = 0.00
        for dim in individual:
            result += (dim - 1) ** 2 - 10 * math.cos(2 * math.pi * (dim - 1))
        return (10 * len(individual) + result)

    def generatePopulation(self, pop_size, dim, bounds):
        for ind in range(pop_size):
            lp = []
            for d in range(dim):
                lp.append(uniform(bounds[d][0], bounds[d][1]))
            self.pop.append(lp)

    def evaluatePopulation(self):
        fpop = []
        for ind in self.pop:
            fpop.append(self.fitness(ind))
        return fpop

    def getBestSolution(self, maximize, fpop):
        fbest = fpop[0]
        best = [values for values in self.pop[0]]
        for ind in range(1, len(self.pop)):
            if maximize == True:
                if fpop[ind] >= fbest:
                    fbest = float(fpop[ind])
                    best = [values for values in self.pop[ind]]
            else:
                if fpop[ind] <= fbest:
                    fbest = float(fpop[ind])
                    best = [values for values in self.pop[ind]]

        return fbest, best

    def rand_1_bin(self, ind, dim, wf, cr):
        p1 = ind
        while (p1 == ind):
            p1 = choice(self.pop)
        p2 = ind
        while (p2 == ind or p2 == p1):
            p2 = choice(self.pop)
        p3 = ind
        while (p3 == ind or p3 == p1 or p3 == p2):
            p3 = choice(self.pop)

        # print('current: %s\n' % str(ind))
        # print('p1: %s\n' % str(p1))
        # print('p2: %s\n' % str(p2))
        # print('p3: %s\n' % str(p3))
        # input('...')

        cutpoint = randint(0, dim - 1)
        candidateSol = []

        # print('cutpoint: %i' % (cutpoint))
        # input('...')

        for i in range(dim):
            if (i == cutpoint or uniform(0, 1) < cr):
                candidateSol.append(p3[i] + wf * (p1[i] - p2[i]))  # -> rand(p3) , vetor diferença (wf*(p1[i]-p2[i]))
            else:
                candidateSol.append(ind[i])

        # print('candidateSol: %s' % str(candidateSol))
        # input('...')
        # print('\n\n')
        return candidateSol

    def currentToBest_2_bin(self, ind, best, dim, wf, cr):
        p1 = ind
        while (p1 == ind):
            p1 = choice(self.pop)
        p2 = ind
        while (p2 == ind or p2 == p1):
            p2 = choice(self.pop)

        # print('current: %s\n' % str(ind))
        # print('p1: %s\n' % str(p1))
        # print('p2: %s\n' % str(p2))
        # input('...')

        cutpoint = randint(0, dim - 1)
        candidateSol = []

        # print('cutpoint: %i' % (cutpoint))
        # input('...')

        for i in range(dim):
            if (i == cutpoint or uniform(0, 1) < cr):
                candidateSol.append(ind[i] + wf * (best[i] - ind[i]) + wf * (
                            p1[i] - p2[i]))  # -> rand(p3) , vetor diferença (wf*(p1[i]-p2[i]))
            else:
                candidateSol.append(ind[i])

        # print('candidateSol: %s' % str(candidateSol))
        # input('...')
        # print('\n\n')
        return candidateSol

    def boundsRes(self, ind, bounds):
        for d in range(len(ind)):
            if ind[d] < bounds[d][0]:
                ind[d] = bounds[d][0]
            if ind[d] > bounds[d][1]:
                ind[d] = bounds[d][1]

    def diferentialEvolution(self, pop_size, dim, bounds, max_iterations, runs, weight_factor=0.8, crossover_rate=0.9,
                             maximize=True, operator=0):
        # generete execution identifier
        uid = uuid.uuid4()
        mkdir(str(uid))
        mkdir(str(uid) + '/graphs')
        # to record the results
        results = open(str(uid) + '/results.txt', 'a')
        records = open(str(uid) + '/records.txt', 'a')
        if operator == 0:
            operatorStr = 'rand/1/bin'
        elif operator == 1:
            operatorStr = 'current to best/2/bin'
        results.write('ID: %s\tDate: %s\tRuns: %s\tOperator: %s\n' % (
        str(uid), strftime("%Y-%m-%d %H:%M:%S", gmtime()), str(runs), operatorStr))
        results.write(
            '=================================================================================================================\n')
        records.write('ID: %s\tDate: %s\tRuns: %s\tOperator: %s\n' % (
        str(uid), strftime("%Y-%m-%d %H:%M:%S", gmtime()), str(runs), operatorStr))
        records.write(
            '=================================================================================================================\n')
        avr_fbest_r = []
        avr_diversity_r = []
        fbest_r = []
        best_r = []
        elapTime_r = []
        # runs
        for r in range(runs):
            elapTime = []
            start = time()
            records.write('Run: %i\n' % r)
            records.write('Iter\tGbest\tAvrFit\tDiver\tETime\t\n')

            # start the algorithm
            best = []  # global best positions
            fbest = 0.00

            # global best fitness
            if maximize == True:
                fbest = 0.00
            else:
                fbest = math.inf

            # initial_generations
            self.generatePopulation(pop_size, dim, bounds)
            fpop = self.evaluatePopulation()

            # print('pop: %s\n' % str(self.pop))
            # print('fpop: %s\n' % str(fpop))

            fbest, best = self.getBestSolution(maximize, fpop)

            # print('fbest: %f\n' % (fbest))
            # print('best: %s\n' % str(best))
            # input('...')

            # evolution_step
            for iteration in range(max_iterations):
                avrFit = 0.00
                # #update_solutions
                for ind in range(0, len(self.pop)):
                    if operator == 0:
                        candSol = self.rand_1_bin(self.pop[ind], dim, weight_factor, crossover_rate)
                    elif operator == 1:
                        candSol = self.currentToBest_2_bin(self.pop[ind], best, dim, weight_factor, crossover_rate)

                    # print('candSol: %s' % str(candSol))

                    self.boundsRes(candSol, bounds)
                    fcandSol = self.fitness(candSol)

                    # print('candSolB: %s' % str(candSol))
                    # print('fcandSol: %f\n' % (fcandSol))

                    if maximize == False:
                        if fcandSol <= fpop[ind]:
                            self.pop[ind] = candSol
                            fpop[ind] = fcandSol
                    else:
                        if fcandSol >= fpop[ind]:
                            self.pop[ind] = candSol
                            fpop[ind] = fcandSol
                    avrFit += fpop[ind]
                avrFit = avrFit / pop_size
                self.diversity.append(self.updateDiversity())

                fbest, best = self.getBestSolution(maximize, fpop)

                self.fbest_list.append(fbest)
                elapTime.append((time() - start) * 1000.0)
                records.write('%i\t%.4f\t%.4f\t%.4f\t%.4f\n' % (
                iteration, round(fbest, 4), round(avrFit, 4), round(self.diversity[iteration], 4), elapTime[iteration]))
            records.write('Pos: %s\n\n' % str(best))
            fbest_r.append(fbest)
            best_r.append(best)
            elapTime_r.append(elapTime[max_iterations - 1])
            self.generateGraphs(self.fbest_list, self.diversity, max_iterations, uid, r)
            avr_fbest_r.append(self.fbest_list)
            avr_diversity_r.append(self.diversity)

            self.pop = []
            self.m_nmdf = 0.00
            self.diversity = []
            self.fbest_list = []

        fbestAux = [sum(x) / len(x) for x in zip(*avr_fbest_r)]
        diversityAux = [sum(x) / len(x) for x in zip(*avr_diversity_r)]
        self.generateGraphs(fbestAux, diversityAux, max_iterations, uid, 'Overall')
        records.write(
            '=================================================================================================================')
        if maximize == False:
            results.write('Gbest Overall: %.4f\n' % (min(fbest_r)))
            results.write('Positions: %s\n\n' % str(best_r[fbest_r.index(min(fbest_r))]))
        else:
            results.write('Gbest Overall: %.4f\n' % (max(fbest_r)))
            results.write('Positions: %s\n\n' % str(best_r[fbest_r.index(max(fbest_r))]))

        results.write('Gbest Average: %.4f\n' % (sum(fbest_r) / len(fbest_r)))
        results.write(
            'Gbest Median: %.4f #probably should use median to represent due probably non-normal distribution (see Shapiro-Wilk normality test)\n' % (
                median(fbest_r)))
        if runs > 1:
            results.write('Gbest Standard Deviation: %.4f\n\n' % (stdev(fbest_r)))
        results.write('Elappsed Time Average: %.4f\n' % (sum(elapTime_r) / len(elapTime_r)))
        if runs > 1:
            results.write('Elappsed Time Standard Deviation: %.4f\n' % (stdev(elapTime_r)))
        results.write(
            '=================================================================================================================\n')


if __name__ == '__main__':
    max_iterations = 100
    pop_size = 20
    dim = 2
    runs = 10
    bounds = ((-5.12, 5.12), (-5.12, 5.12))
    p = DE()
    p.diferentialEvolution(pop_size, dim, bounds, max_iterations, runs, maximize=False, operator=0)