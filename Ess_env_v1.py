import numpy as np
import random
from collections import deque

class EnergyStorage:
    def __init__(self, capacity=100, max_charge_rate=25, max_discharge_rate=25, efficiency=0.95):
        self.capacity = 200         # 储能容量 (kWh)
        self.soc = 0.5 * capacity   # 初始电量设为50%
        self.max_charge = 100       # 最大充电功率 (kW)
        self.max_discharge = -100   # 最大放电功率 (kW)
        self.efficiency = 0.95      # 充放电效率

    def step(self, action):
        # action范围[-1,1]，负数放电，正数充电
        actual_action = action * (self.max_charge if action > 0 else self.max_discharge)
        
        if actual_action > 0:  # 充电
            energy = min(actual_action * self.efficiency, self.capacity - self.soc)
            self.soc += energy
        else:  # 放电
            energy = max(actual_action / self.efficiency, -self.soc)
            self.soc += energy
        
        return energy
