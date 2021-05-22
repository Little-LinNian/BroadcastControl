from typing import TYPE_CHECKING, Any, Callable, Type, Union

if TYPE_CHECKING:
    from graia.broadcast.interfaces.dispatcher import DispatcherInterface

T_Dispatcher = Union[
    Type["BaseDispatcher"], "BaseDispatcher", Callable[["DispatcherInterface"], Any]
]

T_Dispatcher_Callable = Callable[["DispatcherInterface"], Any]

DEFAULT_LIFECYCLE_NAMES = (
    "beforeDispatch",
    "afterDispatch",
    "beforeExecution",
    "afterExecution",
    "beforeTargetExec",
    "afterTargetExec",
)

from graia.broadcast.entities.dispatcher import BaseDispatcher
