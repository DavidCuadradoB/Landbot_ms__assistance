from dependency_injector import containers, providers

from assistance.application.EventServiceImpl import EventServiceImpl


class Container(containers.DeclarativeContainer):
    event_service = providers.Factory(

        EventServiceImpl
    )
