# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Profiler to check if there are any bottlenecks in your code."""
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Optional, Union

from pytorch_lightning.profilers.profiler import Profiler
from pytorch_lightning.utilities.rank_zero import rank_zero_deprecation


class AbstractProfiler(ABC):
    """Specification of a profiler.

    See deprecation warning below

    .. deprecated:: v1.6
        `AbstractProfiler` was deprecated in v1.6 and will be removed in v1.8.
        Please use `Profiler` instead.
    """

    @abstractmethod
    def start(self, action_name: str) -> None:
        """Defines how to start recording an action."""

    @abstractmethod
    def stop(self, action_name: str) -> None:
        """Defines how to record the duration once an action is complete."""

    @abstractmethod
    def summary(self) -> str:
        """Create profiler summary in text format."""

    @abstractmethod
    def setup(self, **kwargs: Any) -> None:
        """Execute arbitrary pre-profiling set-up steps as defined by subclass."""

    @abstractmethod
    def teardown(self, **kwargs: Any) -> None:
        """Execute arbitrary post-profiling tear-down steps as defined by subclass."""


class BaseProfiler(Profiler):
    """
    .. deprecated:: v1.6
        `BaseProfiler` was deprecated in v1.6 and will be removed in v1.8.
        Please use `Profiler` instead.
    """

    def __init__(self, dirpath: Optional[Union[str, Path]], filename: Optional[str]):
        rank_zero_deprecation(
            "`BaseProfiler` was deprecated in v1.6 and will be removed in v1.8. Please use `Profiler` instead."
        )
        super().__init__(dirpath=dirpath, filename=filename)


class PassThroughProfiler(Profiler):
    """This class should be used when you don't want the (small) overhead of profiling.

    The Trainer uses this class by default.
    """

    def start(self, action_name: str) -> None:
        pass

    def stop(self, action_name: str) -> None:
        pass
