"""Runs the algorithm for the three main steps."""
from init import *
from math import *


def gethealth(bact):
    return bact.health


def reproduction(population):
    # sort the population in order of increasing health value
    population = sorted(population, key=gethealth, reverse=False)

    # Sr healthiest bacteria split into two bacteria, which are placed at the
    # same location
    i, j = S-Sr, 0
    while j < Sr:
        population[i] = population[j]
        i, j = i+1, j+1

    for i in range(S):
        population[i].health = 0.0
    return population


def elimination_dispersal(num, population, c_space, fe_count, best, c_prob):
    """
    Elimination and dispersal event.
    """
    for i in range(S):
        # simply disperse bacterium to a random location on the search space
        c_prob = map_func(num, c_prob, i+1)
        if c_prob < p_ed:
            for j in range(dimension):
                c_space = map_func(num, c_space, i+j+1)
                population[i].vect[j] = c_space
            population[i], fe_count, best = rosenbrock(
                population[i], fe_count, best)

    return population, c_space, fe_count, best, c_prob


def interaction(x):
    attract, repel, diff = 0.0, 0.0, 0.0
    for i in range(S):
        diff = 0.0
        for j in range(dimension):
            diff += pow(x.vect[j] - population[i].vect[j], 2.0)

        attract += -1.0*d_attr*exp(-1.0*w_attr*diff)
        repel += h_rep*exp(-1.0*w_rep*diff)

    # this produces the swarming effect
    x.fitness = x.cost + attract + repel
    return x


def tumble_step(num, new_cell, current_cell, c_tumble):
    temp1, temp2 = 0.0, 0.0
    for i in range(dimension):
        c_tumble = map_func(num, c_tumble, i+1)
        delta[i] = c_tumble
        temp1 += pow(delta[i], 2.0)

    temp2 = sqrt(temp1)
    for i in range(dimension):
        rand_vect[i] = delta[i]/temp2
        new_cell.vect[i] = current_cell.vect[
            i] + current_cell.step_size*rand_vect[i]
        # There is no need to perform search outside of the given bounds.
        if new_cell.vect[i] < space[i][0]:
            new_cell.vect[i] = space[i][0]
        if new_cell.vect[i] > space[i][1]:
            new_cell.vect[i] = space[i][1]
    return new_cell, c_tumble


def swim_step(new_cell, current_cell):

    for i in range(dimension):
        new_cell.vect[i] = new_cell.vect[
            i] + current_cell.step_size*rand_vect[i]
        # there is no need to perform search outside of the given bounds
        if new_cell.vect[i] < space[i][0]:
            new_cell.vect[i] = space[i][0]
        if new_cell.vect[i] > space[i][1]:
            new_cell.vect[i] = space[i][1]
    return new_cell


def chemotaxis(num, population, fe_count, best, c_tumble):
    # TODO: Check code!
    Jlast = 0.0
    new_cell = Cell()
    for i in range(S):
        population[i] = interaction(population[i])
        Jlast = population[i].fitness
        # new_cell = Cell()
        # tumble i bactu nd save new cell
        new_cell, c_tumble = tumble_step(
            num, new_cell, population[i], c_tumble)
        new_cell, fe_count, best = rosenbrock(new_cell, fe_count, best)
        new_cell = interaction(new_cell)
        for j in range(dimension):
            population[i].vect[j] = new_cell.vect[j]
        population[i].cost = new_cell.cost
        population[i].fitness = new_cell.fitness
        population[i].health += population[i].fitness

        for m in range(N_sl):
            if new_cell.fitness < Jlast:
                Jlast = new_cell.fitness
                new_cell = swim_step(new_cell, population[i])

                new_cell, fe_count, best = rosenbrock(new_cell, fe_count, best)
                new_cell = interaction(new_cell)

                # copy
                for j in range(dimension):
                    population[i].vect[j] = new_cell.vect[j]
                population[i].cost = new_cell.cost
                population[i].fitness = new_cell.fitness
                population[i].health += population[i].fitness

            else:
                break
    return population, fe_count, best


def optimization(num, population, c_space, fe_count, best, c_prob, c_tumble):
    for l in range(N_ed):

        for k in range(N_re):

            for j in range(N_ch):
                population, fe_count, best = chemotaxis(
                    num, population, fe_count, best, c_tumble)
                # print("best = %d, fe_count = %d", (best, fe_count))

            population = reproduction(population)
        print("best = ", best, " fe_count = ", fe_count)
        population, c_space, fe_count, best, c_prob = elimination_dispersal(
            num, population, c_space, fe_count, best, c_prob)

    print("best found value: ", best, " number of function evaluations: ",
          fe_count, " For Chaotic map ", num)
    return best
