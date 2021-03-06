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


def elimination_dispersal(num, population, space, fe_count, best):
    """
    Elimination and dispersal event.
    """
    for i in range(S):
        # simply disperse bacterium to a random location on the search space
        # c_prob = 0.2
        c_prob = random_val(0.0, 1.0)
        if c_prob < p_ed:
            for j in range(dimension):
                population[i].vect[j] = random_val(space[j][0], space[j][1])
            population[i], fe_count, best = objective_function(
                num, population[i], fe_count, best)

    return population, fe_count, best


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


def tumble_step(new_cell, current_cell):
    a, b, temp1, temp2 = -1.0, 1.0, 0.0, 0.0
    for i in range(dimension):
        # c_tumble = 0.1
        c_tumble = random_val(a, b)
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
    return new_cell


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


def chemotaxis(num, population, fe_count, best):
    # TODO: Check code!
    Jlast = 0.0
    new_cell = Cell()
    for i in range(S):
        population[i] = interaction(population[i])
        Jlast = population[i].fitness
        # new_cell = Cell()
        # tumble i bactu nd save new cell
        new_cell = tumble_step(new_cell, population[i])
        new_cell, fe_count, best = objective_function(
            num, new_cell, fe_count, best)
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

                new_cell, fe_count, best = objective_function(
                    num, new_cell, fe_count, best)
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


def optimization(num, population, space, fe_count, best):
    for l in range(N_ed):

        for k in range(N_re):

            for j in range(N_ch):
                population, fe_count, best = chemotaxis(
                    num, population, fe_count, best)
                # print("best = %d, fe_count = %d", (best, fe_count))

            population = reproduction(population)
        print("best = ", best, " fe_count = ", fe_count)
        population, fe_count, best = elimination_dispersal(
            num, population, space, fe_count, best)

    print("best found value: ", best, " number of function evaluations: ",
          fe_count, " For Fitness function ", num)
    return best
